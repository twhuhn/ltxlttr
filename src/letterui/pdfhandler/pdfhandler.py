import os
import uuid 

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

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

def generate_letter_template(data: dict, templatename: str = 'default.jinja2'):
  """
  Generates the letter from a template and returns the latex string.
  """
  TEMPLATE_DIR = Path(__file__).resolve().parent.parent.parent / 'latextemplates'
  TEMPLATE_PATH = TEMPLATE_DIR / templatename
  
  try:
    fsloader = FileSystemLoader(TEMPLATE_DIR)
    env = Environment(loader=fsloader)

  except FileNotFoundError:
    raise('No such Template named ' + templatename + 'or template was not found')

  return env.get_template(templatename).render(data)
