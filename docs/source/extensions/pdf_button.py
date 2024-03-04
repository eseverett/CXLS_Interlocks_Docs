### This python file is a custom directory for making a button that links to a PDF. 

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class PDFButtonDirective(SphinxDirective):
    has_content = True
    required_arguments = 1  # Only the PDF file name is required as an argument
    optional_arguments = 1  # No optional arguments
    final_argument_whitespace = False  # Argument does not consume trailing whitespace

    def run(self):
        pdf_filename = self.arguments[0]
        # Prepend the path to `_static` to the PDF filename
        # Adjust this path if your static files are located differently
        pdf_path = f'/_static/{pdf_filename}'
        
        # Use the provided content as the button text if available, otherwise default to the PDF filename
        button_text = ' '.join(self.content) if self.content else pdf_filename
        
        # Construct the HTML for the button
        button_html = f'<a href="{pdf_path}" class="pdf-button" target="_blank">{button_text}</a>'
        return [nodes.raw('', button_html, format='html')]

def setup(app):
    app.add_directive("pdfbutton", PDFButtonDirective)
