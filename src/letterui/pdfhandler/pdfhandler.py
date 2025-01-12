import os
from .templating import generate_letter_template as gentemplate

def create_pdf(message):
    # Create a PDF file
    # Create a temporary folder with a UUID as its name
    temp_folder = os.path.join("/tmp/ltxlttr", str(uuid.uuid4()))
    os.makedirs(temp_folder, exist_ok=False) # @TODO try catch

    # Create a file input.tex in this folder with message as content
    tex_file_path = os.path.join(temp_folder, "input.tex")
    pdf_file_path = os.path.join(temp_folder, "input.pdf")
    with open(tex_file_path, "w") as tex_file:
        tex_file.write(message)

    # Run pdflatex on this file
    os.system(f"pdflatex -output-directory={temp_folder} {tex_file_path}")
    return pdf_file_path

def generate_letter_template(form):
    return gentemplate(form)
