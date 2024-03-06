### This python file is a custom directory for making a button that links to a PDF. 

from docutils import nodes
from sphinx.util.docutils import SphinxDirective
import os

class PDFButtonDirective(SphinxDirective):
    has_content = True
    required_arguments = 1  # Only the PDF file name is required as an argument
    optional_arguments = 1  # No optional arguments
    final_argument_whitespace = False  # Argument does not consume trailing whitespace

    def run(self):
        pdf_filename = self.arguments[0]
        # Prepend the path to `_static` to the PDF filename
        # Adjust this path if your static files are located differently
        # pdf_path = f'/_static/{pdf_filename}'
        # pdf_path = f'/docs/build/html/_static/{pdf_filename}'    
        
        # Check if explicitly marked as a local build
        
        on_gitlab = os.environ.get('GITLAB_CI') == 'true'
        on_github = os.environ.get('ON_GITHUB') == 'true' # custom environment variable

        if on_gitlab:
            pdf_path = f'/_static/{pdf_filename}'
        elif on_github:
            pdf_path = f'/_static/{pdf_filename}'
        else:
            # Default to local development path
            pdf_path = f'/docs/build/html/_static/{pdf_filename}'          
        
        
        
        
        # Use the provided content as the button text if available, otherwise default to the PDF filename
        button_text = ' '.join(self.content) if self.content else pdf_filename
        
        # Construct the HTML for the button
        button_html = f'<a href="{pdf_path}" class="pdf-button" target="_blank">{button_text}</a>'
        return [nodes.raw('', button_html, format='html')]

def setup(app):
    app.add_directive("pdfbutton", PDFButtonDirective)
