from django.shortcuts import render, render_to_response
#from knowledge.models import *
from pacscon.models import Patient, System, PatientJpeg
import json

def defaultVieworg(request):
    final = []
    for x in range(len(System.which_system)):
        if Patient.objects.filter(system=System.which_system[x][0]):
            yo = []
            yo.append(System.which_system[x][1])
            jax = []
            for e in Patient.objects.filter(system=System.which_system[x][0]):
                jax.append([e.pk, e.pat_id, e.diagnosis.diagnosis, "DICOM"])
            yo.append(jax)
            final.append(yo)
    list = json.dumps(final)
    return render(request, 'knowledge/main.html', {
        'list': list,
    })


def defaultView(request):
    final = []
    for x in System.which_system:
            system = []
            system.append(x[1])
            jax = []
            for e in PatientJpeg.objects.filter(system=x[0]):
                    jax.append([e.pk, '', e.diagnosis.diagnosis, "JPEG"])
            for e in Patient.objects.filter(system=x[0]):
                    jax.append([e.pk, e.pat_id, e.diagnosis.diagnosis, "DICOM"])
            system.append(jax)
            final.append(system)
    list = json.dumps(final)
    return render(request, 'knowledge/main.html', {
        'list': list,
    })

def viewDCMCase(request, patID):
    patient = Patient.objects.get(pk=patID)
    return render_to_response("knowledge/case.html", {'patient': patient,
    })

def viewJPEGCase(request, patID):
    patient = PatientJpeg(patID)
    return render_to_response("knowledge/caseJPEG.html", {'patient': patient})
