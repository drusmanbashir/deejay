# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Ae(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    aet = models.CharField(max_length=160, unique=True)
    hostname = models.CharField(max_length=160)
    port = models.IntegerField()
    cipher_suites = models.CharField(max_length=160, blank=True)
    pat_id_issuer = models.CharField(max_length=160, blank=True)
    acc_no_issuer = models.CharField(max_length=160, blank=True)
    user_id = models.CharField(max_length=160, blank=True)
    passwd = models.CharField(max_length=160, blank=True)
    fs_group_id = models.CharField(max_length=160, blank=True)
    ae_group = models.CharField(max_length=160, blank=True)
    ae_desc = models.CharField(max_length=160, blank=True)
    wado_url = models.CharField(max_length=160, blank=True)
    station_name = models.CharField(max_length=160, blank=True)
    institution = models.CharField(max_length=160, blank=True)
    department = models.CharField(max_length=160, blank=True)
    installed = models.BooleanField()
    vendor_data = models.CharField(max_length=160, blank=True) # This field type is a guess.

    class Meta:
        db_table = 'ae'

class Code(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    code_value = models.CharField(max_length=160)
    code_designator = models.CharField(max_length=160)
    code_version = models.CharField(max_length=160, blank=True)
    code_meaning = models.CharField(max_length=160, blank=True)

    class Meta:
        db_table = 'code'

class ContentItem(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    instance_fk = models.ForeignKey('Instance', null=True, db_column='instance_fk', blank=True)
    name_fk = models.ForeignKey(Code, null=True, db_column='name_fk', blank=True, related_name='+')
    code_fk = models.ForeignKey(Code, null=True, db_column='code_fk', blank=True, related_name='+')
    rel_type = models.CharField(max_length=160, blank=True)
    text_value = models.CharField(max_length=160, blank=True)

    class Meta:
        db_table = 'content_item'

class Files(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    instance_fk = models.ForeignKey('Instance', null=True, db_column='instance_fk', blank=True)
    filesystem_fk = models.ForeignKey('Filesystem', null=True, db_column='filesystem_fk', blank=True)
    filepath = models.CharField(max_length=160)
    file_tsuid = models.CharField(max_length=160)
    file_md5 = models.CharField(max_length=160, blank=True)
    file_size = models.IntegerField(null=True, blank=True)
    file_status = models.IntegerField(null=True, blank=True)
    md5_check_time = models.DateTimeField(null=True, blank=True)
    created_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'files'

class Filesystem(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    next_fk = models.ForeignKey('self', null=True, db_column='next_fk', blank=True)
    dirpath = models.CharField(max_length=160, unique=True)
    fs_group_id = models.CharField(max_length=160)
    retrieve_aet = models.CharField(max_length=160)
    availability = models.IntegerField()
    fs_status = models.IntegerField()
    user_info = models.CharField(max_length=160, blank=True)

    class Meta:
        db_table = 'filesystem'

class Gppps(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    patient_fk = models.ForeignKey('Patient', null=True, db_column='patient_fk', blank=True)
    pps_iuid = models.CharField(max_length=160, unique=True)
    pps_start = models.DateTimeField(null=True, blank=True)
    pps_status = models.IntegerField()
    created_time = models.DateTimeField(null=True, blank=True)
    updated_time = models.DateTimeField(null=True, blank=True)
    pps_attrs = models.CharField(max_length=160, blank=True) # This field type is a guess.

    class Meta:
        db_table = 'gppps'

class Gpsps(models.Model):
    id= models.IntegerField(primary_key=True, db_column='pk')
    patient_fk = models.ForeignKey('Patient', null=True, db_column='patient_fk', blank=True)
    code_fk = models.ForeignKey(Code, null=True, db_column='code_fk', blank=True)
    gpsps_iuid = models.CharField(max_length=160, unique=True)
    gpsps_tuid = models.CharField(max_length=160, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)
    gpsps_status = models.IntegerField(null=True, blank=True)
    gpsps_prior = models.IntegerField(null=True, blank=True)
    in_availability = models.IntegerField(null=True, blank=True)
    item_attrs = models.CharField(max_length=160, blank=True) # This field type is a guess.

    class Meta:
        db_table = 'gpsps'

class Instance(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    series_fk = models.ForeignKey('Series', null=True, db_column='series_fk', blank=True)
    srcode_fk = models.ForeignKey(Code, null=True, db_column='srcode_fk', blank=True)
    media_fk = models.ForeignKey('Media', null=True, db_column='media_fk', blank=True)
    sop_iuid = models.CharField(max_length=160, unique=True)
    sop_cuid = models.CharField(max_length=160)
    inst_no = models.CharField(max_length=160, blank=True)
    content_datetime = models.DateTimeField(null=True, blank=True)
    sr_complete = models.CharField(max_length=160, blank=True)
    sr_verified = models.CharField(max_length=160, blank=True)
    inst_custom1 = models.CharField(max_length=160, blank=True)
    inst_custom2 = models.CharField(max_length=160, blank=True)
    inst_custom3 = models.CharField(max_length=160, blank=True)
    ext_retr_aet = models.CharField(max_length=160, blank=True)
    retrieve_aets = models.CharField(max_length=160, blank=True)
    availability = models.IntegerField()
    inst_status = models.IntegerField()
    all_attrs = models.BooleanField()
    commitment = models.BooleanField()
    archived = models.BooleanField()
    created_time = models.DateTimeField(null=True, blank=True)
    updated_time = models.DateTimeField(null=True, blank=True)
    inst_attrs = models.CharField(max_length=160, blank=True) # This field type is a guess.

    class Meta:
        db_table = 'instance'

class Issuer(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    entity_id = models.CharField(max_length=160, unique=True, blank=True)
    entity_uid = models.CharField(max_length=160, blank=True)
    entity_uid_type = models.CharField(max_length=160, blank=True)

    class Meta:
        db_table = 'issuer'

class Media(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    fileset_iuid = models.CharField(max_length=160, unique=True)
    fileset_id = models.CharField(max_length=160, blank=True)
    media_rq_iuid = models.CharField(max_length=160, blank=True)
    media_status = models.IntegerField()
    media_status_info = models.CharField(max_length=160, blank=True)
    media_usage = models.IntegerField()
    created_time = models.DateTimeField(null=True, blank=True)
    updated_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'media'

class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True, db_column='pk')
    diagnosis = models.CharField(max_length=160)

    class Meta:
        db_table = 'diagnosis'

    def __unicode__(self):
        return self.diagnosis

class System (models.Model):
        HN = 'HN'
        CHEST = 'CH'
        CARDIAC = 'CA'
        CNS = 'CN'
        MSK = 'MS'
        PAEDS = 'PA'
        GI = 'GI'
        HPB = 'HPB'
        GU = 'GU'
        VAS = 'VA'
        BRE = 'BR'
        which_system = (
            (HN, 'Head & Neck'),
            (BRE, 'Breast'),
            (CHEST, 'Chest'),
            (CARDIAC, 'Cardiac'),
            (CNS, 'Neuro'),
            (HPB, 'Hepatobiliary'),
            (MSK, 'MSK'),
            (PAEDS, 'Paediatrics'),
            (GI, 'Gastrointestinal'),
            (GU, 'Genitourinary'),
            (VAS, 'Vascular'),
        )


class Mpps(models.Model):
    pk = models.IntegerField(primary_key=True)
    patient_fk = models.ForeignKey('Patient', null=True, db_column='patient_fk', blank=True)
    drcode_fk = models.ForeignKey(Code, null=True, db_column='drcode_fk', blank=True)
    mpps_iuid = models.CharField(max_length=160, unique=True)
    pps_start = models.DateTimeField(null=True, blank=True)
    station_aet = models.CharField(max_length=160, blank=True)
    modality = models.CharField(max_length=160, blank=True)
    accession_no = models.CharField(max_length=160, blank=True)
    mpps_status = models.IntegerField()
    created_time = models.DateTimeField(null=True, blank=True)
    updated_time = models.DateTimeField(null=True, blank=True)
    mpps_attrs = models.CharField(max_length=160, blank=True) # This field type is a guess.

    class Meta:
        db_table = 'mpps'

class MwlItem(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    patient_fk = models.ForeignKey('Patient', null=True, db_column='patient_fk', blank=True)
    sps_status = models.IntegerField(null=True, blank=True)
    sps_id = models.CharField(max_length=160, blank=True)
    start_datetime = models.DateTimeField()
    station_aet = models.CharField(max_length=160)
    station_name = models.CharField(max_length=160, blank=True)
    modality = models.CharField(max_length=160)
    perf_physician = models.CharField(max_length=160, blank=True)
    perf_phys_fn_sx = models.CharField(max_length=160, blank=True)
    perf_phys_gn_sx = models.CharField(max_length=160, blank=True)
    perf_phys_i_name = models.CharField(max_length=160, blank=True)
    perf_phys_p_name = models.CharField(max_length=160, blank=True)
    req_proc_id = models.CharField(max_length=160)
    accession_no = models.CharField(max_length=160, blank=True)
    study_iuid = models.CharField(max_length=160)
    created_time = models.DateTimeField(null=True, blank=True)
    updated_time = models.DateTimeField(null=True, blank=True)
    item_attrs = models.CharField(max_length=160, blank=True) # This field type is a guess.

    class Meta:
        db_table = 'mwl_item'

class OtherPid(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    pat_id = models.CharField(max_length=160)
    pat_id_issuer = models.CharField(max_length=160)

    class Meta:
        db_table = 'other_pid'

class Patient(models.Model):
    id = models.AutoField(primary_key=True, db_column='pk')
    merge_fk = models.ForeignKey('self', null=True, db_column='merge_fk', blank=True)
    pat_id = models.CharField(max_length=160, blank=True)
    pat_id_issuer = models.CharField(max_length=160, blank=True)
    pat_name = models.CharField(max_length=160, blank=True)
    pat_fn_sx = models.CharField(max_length=160, blank=True)
    pat_gn_sx = models.CharField(max_length=160, blank=True)
    pat_i_name = models.CharField(max_length=160, blank=True)
    pat_p_name = models.CharField(max_length=160, blank=True)
    pat_birthdate = models.CharField(max_length=160, blank=True)
    pat_sex = models.CharField(max_length=160, blank=True)
    pat_custom1 = models.CharField(max_length=160, blank=True)
    pat_custom2 = models.CharField(max_length=160, blank=True)
    pat_custom3 = models.CharField(max_length=160, blank=True)
    created_time = models.DateTimeField(null=True, blank=True)
    updated_time = models.DateTimeField(null=True, blank=True)
    pat_attrs = models.CharField(max_length=160, blank=True) # This field type is a guess.
    description = models.TextField(blank=True)
    diagnosis = models.ForeignKey('Diagnosis', db_column='diagnosis_fk', blank=True)
    system = models.CharField(max_length=3, choices=System.which_system)

    class Meta:
        db_table = 'patient'

    def __unicode__(self):
        return u"%s" % self.pk

class Roles(models.Model):
    user = models.ForeignKey('Users', null=True, blank=True)
    roles = models.CharField(max_length=160, blank=True)

    class Meta:
        db_table = 'roles'

class Series(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    study_fk = models.ForeignKey('Study', null=True, db_column='study_fk', blank=True)
    mpps_fk = models.ForeignKey(Mpps, null=True, db_column='mpps_fk', blank=True)
    inst_code_fk = models.ForeignKey(Code, null=True, db_column='inst_code_fk', blank=True)
    series_iuid = models.CharField(max_length=160, unique=True)
    series_no = models.CharField(max_length=160, blank=True)
    modality = models.CharField(max_length=160, blank=True)
    body_part = models.CharField(max_length=160, blank=True)
    laterality = models.CharField(max_length=160, blank=True)
    series_desc = models.CharField(max_length=160, blank=True)
    institution = models.CharField(max_length=160, blank=True)
    station_name = models.CharField(max_length=160, blank=True)
    department = models.CharField(max_length=160, blank=True)
    perf_physician = models.CharField(max_length=160, blank=True)
    perf_phys_fn_sx = models.CharField(max_length=160, blank=True)
    perf_phys_gn_sx = models.CharField(max_length=160, blank=True)
    perf_phys_i_name = models.CharField(max_length=160, blank=True)
    perf_phys_p_name = models.CharField(max_length=160, blank=True)
    pps_start = models.DateTimeField(null=True, blank=True)
    pps_iuid = models.CharField(max_length=160, blank=True)
    series_custom1 = models.CharField(max_length=160, blank=True)
    series_custom2 = models.CharField(max_length=160, blank=True)
    series_custom3 = models.CharField(max_length=160, blank=True)
    num_instances = models.IntegerField()
    src_aet = models.CharField(max_length=160, blank=True)
    ext_retr_aet = models.CharField(max_length=160, blank=True)
    retrieve_aets = models.CharField(max_length=160, blank=True)
    fileset_iuid = models.CharField(max_length=160, blank=True)
    fileset_id = models.CharField(max_length=160, blank=True)
    availability = models.IntegerField()
    series_status = models.IntegerField()
    created_time = models.DateTimeField(null=True, blank=True)
    updated_time = models.DateTimeField(null=True, blank=True)
    series_attrs = models.CharField(max_length=160, blank=True) # This field type is a guess.

    class Meta:
        db_table = 'series'

class SeriesReq(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    series_fk = models.ForeignKey(Series, null=True, db_column='series_fk', blank=True)
    accno_issuer_fk = models.ForeignKey(Issuer, null=True, db_column='accno_issuer_fk', blank=True)
    accession_no = models.CharField(max_length=160, blank=True)
    study_iuid = models.CharField(max_length=160, blank=True)
    req_proc_id = models.CharField(max_length=160, blank=True)
    sps_id = models.CharField(max_length=160, blank=True)
    req_service = models.CharField(max_length=160, blank=True)
    req_physician = models.CharField(max_length=160, blank=True)
    req_phys_fn_sx = models.CharField(max_length=160, blank=True)
    req_phys_gn_sx = models.CharField(max_length=160, blank=True)
    req_phys_i_name = models.CharField(max_length=160, blank=True)
    req_phys_p_name = models.CharField(max_length=160, blank=True)

    class Meta:
        db_table = 'series_req'

class Study(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    patient_fk = models.ForeignKey(Patient, null=True, db_column='patient_fk', blank=True)
    accno_issuer_fk = models.ForeignKey(Issuer, null=True, db_column='accno_issuer_fk', blank=True)
    study_iuid = models.CharField(max_length=160, unique=True)
    study_id = models.CharField(max_length=160, blank=True)
    study_datetime = models.DateTimeField(null=True, blank=True)
    accession_no = models.CharField(max_length=160, blank=True)
    ref_physician = models.CharField(max_length=160, blank=True)
    ref_phys_fn_sx = models.CharField(max_length=160, blank=True)
    ref_phys_gn_sx = models.CharField(max_length=160, blank=True)
    ref_phys_i_name = models.CharField(max_length=160, blank=True)
    ref_phys_p_name = models.CharField(max_length=160, blank=True)
    study_desc = models.CharField(max_length=160, blank=True)
    study_custom1 = models.CharField(max_length=160, blank=True)
    study_custom2 = models.CharField(max_length=160, blank=True)
    study_custom3 = models.CharField(max_length=160, blank=True)
    study_status_id = models.CharField(max_length=160, blank=True)
    mods_in_study = models.CharField(max_length=160, blank=True)
    cuids_in_study = models.CharField(max_length=160, blank=True)
    num_series = models.IntegerField()
    num_instances = models.IntegerField()
    ext_retr_aet = models.CharField(max_length=160, blank=True)
    retrieve_aets = models.CharField(max_length=160, blank=True)
    fileset_iuid = models.CharField(max_length=160, blank=True)
    fileset_id = models.CharField(max_length=160, blank=True)
    availability = models.IntegerField()
    study_status = models.IntegerField()
    checked_time = models.DateTimeField(null=True, blank=True)
    created_time = models.DateTimeField(null=True, blank=True)
    updated_time = models.DateTimeField(null=True, blank=True)
    study_attrs = models.CharField(max_length=160, blank=True) # This field type is a guess.
    description = models.CharField(max_length=400, blank=True)

    class Meta:
        db_table = 'study'

    def __unicode__(self):
        return u"%s" % self.pk


class Users(models.Model):
    user_id = models.CharField(max_length=160, primary_key=True)
    passwd = models.CharField(max_length=160, blank=True)

    class Meta:
        db_table = 'users'

class VerifyObserver(models.Model):
    id = models.IntegerField(primary_key=True, db_column='pk')
    instance_fk = models.ForeignKey(Instance, null=True, db_column='instance_fk', blank=True)
    verify_datetime = models.DateTimeField(null=True, blank=True)
    observer_name = models.CharField(max_length=160, blank=True)
    observer_fn_sx = models.CharField(max_length=160, blank=True)
    observer_gn_sx = models.CharField(max_length=160, blank=True)
    observer_i_name = models.CharField(max_length=160, blank=True)
    observer_p_name = models.CharField(max_length=160, blank=True)

    class Meta:
        db_table = 'verify_observer'
