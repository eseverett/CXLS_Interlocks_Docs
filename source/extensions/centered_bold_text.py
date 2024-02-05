


from docutils import nodes
from sphinx.util.docutils import SphinxDirective

# class TableCaption(SphinxDirective):
#     has_content = True

#     def run(self):
#         # Initialize a paragraph node for the entire caption.
#         paragraph_node = nodes.paragraph('', '', classes=['table-caption'])

#         # Process the directive content as a single string.
#         caption_text = ' '.join(self.content)

#         # Identify and process bold parts, marked by '**', inline.
#         parts = caption_text.split('**')
#         for i, part in enumerate(parts):
#             if i % 2 == 0:
#                 # Regular text parts.
#                 if part:  # Check to avoid adding empty nodes.
#                     paragraph_node += nodes.Text(part)
#             else:
#                 # Bold text parts.
#                 emphasis_node = nodes.strong('', part)
#                 paragraph_node.append(emphasis_node)

#         return [paragraph_node]

# def setup(app):
#     app.add_directive("tablecaption", TableCaption)
#     app.add_css_file('custom.css')  # Ensure this CSS file is in your _static directory.



# Assuming there's a way to mark the preceding table for tight coupling with the caption
class TableCaption(SphinxDirective):
    has_content = True

    def run(self):
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
    app.add_directive("tablecaption", TableCaption)  # Make sure this matches your class name
    app.add_css_file('custom.css')  # If you're using custom CSS

