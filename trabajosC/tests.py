from pylovepdf.tools.officepdf import OfficeToPdf
import os
import glob

def ppt_to_pdf(pptx_file_path, pdf_file_path):
    pptx_file = OfficeToPdf('project_public_5697cc3601ebe170a2268b01fbb87196_7LtLPd51b5090b8c5b06ea21af86aee9cea95', verify_ssl=True, proxies=None)
    # Carga el archivo a convertir
    pptx_file.add_file(pptx_file_path)
    pptx_file.debug = True
    pptx_file.set_output_folder(pdf_file_path)

    pptx_file.execute()
    pptx_file.download()
    
    pptx_file.delete_current_task()

    def get_latest_file(path):
        list_of_files = glob.glob(path + '/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file

    latest_pdf = get_latest_file(output_path)

    new_name = 'EP04.pdf'
    os.rename(latest_pdf, os.path.join(output_path, new_name))

input_path = "media/manuscritos/8° Curso internacional de Trauma/EP04.pptx"
output_path = "media/manuscritos/8° Curso internacional de Trauma/"

ppt_to_pdf(input_path, output_path)



