
### This is a custom sphinx extension that adds the ability to center text and make it bold using a custom directive.

from docutils import nodes
from sphinx.util.docutils import SphinxDirective
class TableCaption(SphinxDirective):
    
    """Custom directive for table captions.

    Args:
        SphinxDirective (): Inherit from the SphinxDirective class

    Returns:
        list: A list of nodes to be added to the document tree
    """
    has_content = True

    def run(self):
        
        """Process the content of the directive.

        Returns:
            list: A list of nodes to be added to the document tree
        """
        
        container = nodes.container(classes=['tight-table-caption-container'])
        caption_paragraph = nodes.paragraph('', '', classes=['table-caption'])

        # Concatenate and process the content as before
        caption_text = ' '.join(self.content)
        parts = caption_text.split('**')
        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part:  # Avoid adding empty nodes
                    caption_paragraph += nodes.Text(part)
            else:
                caption_paragraph += nodes.strong('', part)

        container += caption_paragraph
        return [container]
    
def setup(app):
    
    """ Add the directive to the Sphinx app.
    """
    
    app.add_directive("table-caption", TableCaption)  # Make sure this matches your class name
    app.add_css_file('custom.css')  # If you're using custom CSS

