import subprocess
from subprocess import  Popen
from django.conf import settings
from pylovepdf.tools.officepdf import OfficeToPdf
import os
import glob

from Evaluador.models import *

LIBRE_OFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

def convert_to_pdf_wd(input_docx, out_folder,new_name):
    """Función para convertir word a pdf desde windows

    Args:
        input_docx (string): ruta y nombre del documento a convertir
        out_folder (string): ruta en donde se guardará el nuevo doc pdf
    """    
    manus_file = OfficeToPdf('project_public_5697cc3601ebe170a2268b01fbb87196_7LtLPd51b5090b8c5b06ea21af86aee9cea95', verify_ssl=True, proxies=None)
    # Carga el archivo a convertir
    manus_file.add_file(input_docx)
    manus_file.debug = False
    manus_file.set_output_folder(out_folder)
    manus_file.execute()
    manus_file.download()    
    manus_file.delete_current_task()

    def get_latest_file(path):
        list_of_files = glob.glob(path + '/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file

    latest_pdf = get_latest_file(out_folder)
    os.rename(latest_pdf, os.path.join(out_folder, new_name))


def generate_pdf_linux(doc_path, path):
    """Función para convertir word a pdf desde linux

    Args:
        doc_path (string): ruta y nombre del documento a convertir
        out_folder (string): ruta en donde se guardará el nuevo doc pdf
    """  
    args = ['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', path, doc_path]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def asignar_plantilla(nombre,Trabajo, User):
    
    if nombre == "eccForm":
        plantillaECC.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "pruebasDXForm":
        plantillaPruebasDX.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "RSyMAForm":
        plantillaRSyMA.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "plantillaSCForm":
        plantillaSERIECASOS.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "plantillaCTForm":
        plantillaCORTETRANSVERSAL.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "casosyControlesForm":
        plantillaCASOSyCONTROLES.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "cohortesForm":
        plantillaCOHORTES.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "ANATOMICOForm":
        plantillaANATOMICOyTC.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "validacionEscalasForm":
        plantillaVALIDACIONESCALAS.objects.create(trabajo=Trabajo, user= User)
    elif nombre == "CongresoForm":
        plantillaCONGRESO.objects.create(trabajo=Trabajo, user= User)
    else:
        plantillaEP.objects.create(trabajo=Trabajo, user= User)