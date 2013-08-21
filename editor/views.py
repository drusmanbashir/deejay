from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from editor.models import ContactForm, ImageFile, Img
from blog.models import Post
import datetime
import numpy as np
import glob
import os
import dicom
from PIL import Image, ImageDraw, ImageFont


def Imag():
    a = np.arange(100).reshape(10, 10)
    width, height = a.shape[0], a.shape[1]
    simple = a.reshape(1, 100).tolist()
    info = [width, height, simple]
    return info 


def defaultView(request):
    data = dicom.read_file("media/images/cor.dcm")
    data2 = dicom.read_file("media/images/cor2.dcm")
    #array = Imag()[2] 
    sample = serializers.serialize("json", Post.objects.all())
    dcmImage1 = show_PIL(data)
    dcmImage2 = show_PIL(data2)
    width=dcmImage1.shape[0]
    height=dcmImage1.shape[1]
    dcmSize = dcmImage1.size
    dcmImage = []
    dcmImage.append(dcmImage1.reshape(1, dcmImage1.size).tolist())
    dcmImage.append(dcmImage2.reshape(1, dcmImage2.size).tolist())
    #dcmImage=np.reshape(dcmImage,(1,dcmImage.size))
    if request.method =='POST':
            form = ContactForm(request.POST, request.FILES)
            newFile=ImageFile(imageFile=request.FILES['file'])
            #finalImage = Image.open(request.FILES['file'])
            #if form.is_valid():

            return render(request, 'editor/main.html', {
                'form': form,
                'width': width,
            })
    else:
            form = ContactForm()

    return render(request, 'editor/main.html', {
        'form': form,
        'width': width,
        'height': height,
        'size': dcmSize,
        'sample': sample,
        'dcm_array': dcmImage
    })


def defaultView_org(request):
        if request.method =='POST' :
            form = ContactForm(request.POST,request.FILES)
            newFile=ImageFile(imageFile=request.FILES['file'])
            newFile.save()
            #if form.is_valid():
            dcmFile=reader("media/uploaded_images/2013/04/20/i0000_0000b.dcm")
            finalImage = show_PIL(dcmFile)
            return render(request,'editor/main.html',{
                    'form':form,
                    'image':finalImage,
            })

        else:
            form = ContactForm()

            return render(request,'editor/main.html',{
                  'form':form,
                  })

def showDICOM(request):
          if request.method =='POST':
                  form = ContactForm(request.POST, request.FILES)
          newFile = ImageFile(imageFile=request.FILES['file'])



def reader(ds):
        import dicom
        plan = dicom.read_file(ds)
        return plan

def getLUT(data,window,level):
        chacha = np.piecewise(data,
                        [data <= (level- 0.5 - (window-1)/2),
                                data > (level - 0.5 + (window - 1)/2)],
                        [0,255, lambda data: ((data - (level - 0.5)) / (window - 1)+0.5) * (255 - 0)])
        return chacha


def show_PIL(dataset, width='xx', level='xx'):
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
                print ("The mode is %s, size is %s",mode,size)

                im = Image.frombuffer(mode, size, dataset.PixelData, "raw", mode, 0, 1)  # Recommended to specify all details by http://www.pythonware.com/library/pil/handbook/image.htm

        else:
                image = getLUT(dataset.pixel_array, width, level)
                im = Image.fromarray(image).convert('L')  # Convert mode to L since LUT has only 256 values: http://www.pythonware.com/library/pil/handbook/image.htm
        return image
