import subprocess
from subprocess import  Popen
from django.conf import settings

from Evaluador.forms import eccForm
from Evaluador.models import plantillaCASOSyCONTROLES, plantillaCOHORTES, plantillaECC, plantillaPruebasDX, plantillaRSyMA, plantillaSERIECASOSyCORTETRANSVERSAL

LIBRE_OFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

def convert_to_pdf_wd(input_docx, out_folder):
    p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir',
               out_folder, input_docx])
    print([LIBRE_OFFICE, '--convert-to', 'pdf', input_docx])
    p.communicate()


def generate_pdf_linux(doc_path, path, timeout=None):
    args = ['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', path, doc_path]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)

def asignar_plantilla(nombre,Trabajo, User):
    
    if nombre == "eccForm":
        plantillaECC.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "pruebasDXForm":
        plantillaPruebasDX.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "RSyMAForm":
        plantillaRSyMA.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "plantillaSCyCTForm":
        plantillaSERIECASOSyCORTETRANSVERSAL.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "casosyControlesForm":
        plantillaCASOSyCONTROLES.objects.create(trabajo=Trabajo, user= User)
    else:
        plantillaCOHORTES.objects.create(trabajo=Trabajo, user= User)