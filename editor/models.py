from django.db import models
from django import forms
import numpy as np
from unidecode import unidecode
import os
import gdcm
import dicom
from PIL import Image


class User(models.Model):
    fn = models.CharField(max_length=10)
    sn = models.CharField(max_length=10)


class Systems(models.Model):
        HN = 'HN'
        CHEST = 'CH'
        CNS = 'CN'
        MSK = 'MS'
        PAEDS = 'PA'
        GI = 'GI'
        GU = 'GU'
        VAS = 'VA'
        BRE = 'BR'
        which_system = (
            (HN, 'Head & Neck'),
            (BRE, 'Breast'),
            (CHEST, 'Chest'),
            (CNS, 'Neuro'),
            (MSK, 'MSK'),
            (PAEDS, 'Paediatrics'),
            (GI, 'Gastrointestinal'),
            (GU, 'Genitourinary'),
            (VAS, 'Vascular'),
        )


class ContactForm (forms.Form):
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField()
    # sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required = False)
    file = forms.FileField()

def Img():
    a = np.arange(100).reshape(10, 10)
    return a

class FilePath(models.Model):
    path = models.CharField(max_length=100)
    folder = models.CharField(max_length=100)

    def __unicode__(self):
        return self.path

    class Meta:
        ordering = ('path',)

    def save(self):
        self.folder = os.path.dirname(self.path)
        super(FilePath, self).save()

class Case(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=300, db_index=True)
    dirTree = models.TextField(blank=True)
    created = models.DateField(db_index=True, auto_now_add=True)
    information = models.CharField(max_length=100, db_index=True)
    system = models.CharField(max_length=2,
                            choices=Systems.which_system,
                            #default=CHEST
                              )
    folder = models.CharField(max_length=20)
    files = models.ManyToManyField(FilePath, blank=True, null=True, through='CaseToFile')
    folder_array = models.CharField(max_length=20, blank=True, null=True)
    user = models.ManyToManyField(User, blank=True, null=True, through='UserToCase')

    def __unicode__(self):
        return self.title

    def parseDir(self):
        final = os.path.join("/home/usman/www/deejay/media/uploaded_images", self.folder)
        dirs = []
        newDir = []
        if os.path.exists(final):
            r = gdcm.Reader()
            for x in os.walk(final):
                dirs.append((unidecode(x[0]), x[2]))
            for size in range(len(dirs)):
                for x in range(len(dirs[size][1])):
                    dirs[size][1][x] = unidecode(os.path.join(dirs[size][0], dirs[size][1][x]))
                    if validate(r, dirs[size][1][x]):
                        data = dicom.read_file(dirs[size][1][x])
                        array = dcmToArray(data)
                        np.save((dirs[size][1][x] + "light"), array)
                        array = rawArray(data)
                        np.save(dirs[size][1][x], array)
                        filePath = FilePath(path=(dirs[size][1][x] + ".npy"))
                        filePath.save()
                        rel = CaseToFile(case=self,
                                file=filePath)
                        rel.save()
                newDir.append((dirs[size][0], [x for x in dirs[size][1] if validate(r, x)]))
        else:
            print ("PATH NOT EXISTS ! ")
        return newDir

    def save(self):
        self.dirTree = self.parseDir()
        super(Case, self).save()


def getLUT(data, window, level):
        chacha = np.piecewise(data,
                        [data <= (level - 0.5 - (window - 1) / 2),
                                data > (level - 0.5 + (window - 1) / 2)],
                        [0, 255, lambda data: ((data - (level - 0.5)) / (window - 1) + 0.5) * (255 - 0)])
        return chacha


def rawArray(dataset):
    return dataset.pixel_array


def dcmToArray(dataset, width='xx', level='xx'):
        if (width == 'xx'):
                width = dataset.WindowWidth
                level = dataset.WindowCenter

        if ('PixelData' not in dataset):
                raise TypeError("Cannot show image -- DICOM dataset does not have pixel data")
        if ('WindowWidth' not in dataset) or ('WindowCenter' not in dataset):
                bits = dataset.BitsAllocated
                samples = dataset.SamplesPerPixel
                if bits == 8 and samples == 1:
                        mode = "L"
                elif bits == 8 and samples == 3:
                        mode = "RGB"
                elif bits == 16:
                        mode = "I;16"  # not sure about this -- PIL source says is 'experimental' and no documentation. Also, should bytes swap depending on endian of file and system??
                else:
                        raise TypeError("Don't know PIL mode for %d BitsAllocated and %d SamplesPerPixel" % (bits, samples))

                # PIL size = (width, height)
                size = (dataset.Columns, dataset.Rows)
                print ("The mode is %s, size is %s", mode, size)

                im = Image.frombuffer(mode, size, dataset.PixelData, "raw", mode, 0, 1)  # Recommended to specify all details by http://www.pythonware.com/library/pil/handbook/image.htm

        else:
                image = getLUT(dataset.pixel_array, width, level)
               # im = Image.fromarray(image).convert('L')  # Convert mode to L since LUT has only 256 values: http://www.pythonware.com/library/pil/handbook/image.htm
        return image

def validate(r, file):
    x = False
    r.SetFileName(file)
    if r.CanRead():
        data = dicom.read_file(file)
        x = "WindowWidth" in data
    return x


class UserToCase(models.Model):
    case = models.ForeignKey(Case)
    user = models.ForeignKey(User)

class CaseToFile(models.Model):
    case = models.ForeignKey(Case)
    file = models.ForeignKey(FilePath)


class ImageFile (models.Model):
    imageFile = models.FileField(upload_to='uploaded_images/%Y/%m/%d')
    annotations_path = models.CharField(max_length=100)
    case = models.ForeignKey(Case)


