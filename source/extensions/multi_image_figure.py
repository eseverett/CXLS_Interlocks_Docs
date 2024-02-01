# from docutils import nodes
# from docutils.parsers.rst import Directive
# from sphinx.util.docutils import SphinxDirective

# class MultiImageFigure(SphinxDirective):
#     has_content = True

#     def run(self):
#         # Create a figure node to wrap images and caption
#         figure_node = nodes.figure('')

#         # Process the content lines
#         for image_path in self.content:
#             # Skip empty lines and the last line (caption)
#             if not image_path.strip() or self.content.index(image_path) == len(self.content) - 1:
#                 continue

#             # Create image node and add to the figure
#             image_node = nodes.image(uri=image_path)
#             figure_node += image_node

#         # The last line of the content is treated as the caption
#         caption_text = self.content[-1]
#         figure_node += nodes.caption('', caption_text)

#         return [figure_node]

# def setup(app):
#     app.add_directive("multiimagefigure", MultiImageFigure)


# from docutils.parsers.rst import Directive
# from sphinx.util.docutils import SphinxDirective
# import os

# class MultiImageFigure(SphinxDirective):
#     has_content = True

#     def run(self):
#         figure_node = nodes.figure('')
#         doc_dir = os.path.dirname(self.state.document.current_source)

#         for line in self.content:
#             if not line.strip() or self.content.index(line) == len(self.content) - 1:
#                 continue

#             # Adjust the path if it's not absolute
#             image_path = line.strip()
#             if not image_path.startswith('/'):
#                 image_path = os.path.join(doc_dir, image_path)
                
#             # Make path relative to source directory
#             rel_path = os.path.relpath(image_path, self.env.srcdir)

#             image_node = nodes.image(uri=rel_path)
#             figure_node += image_node

#         caption_text = self.content[-1].strip()
#         figure_node += nodes.caption('', caption_text)

#         return [figure_node]

#     def setup(app):
#         app.add_directive("multiimagefigure", MultiImageFigure)




from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.docutils import SphinxDirective
import os

class MultiImageFigure(SphinxDirective):
    has_content = True

    def run(self):
        figure_node = nodes.figure('')
        doc_dir = os.path.dirname(os.path.relpath(self.state.document.current_source, self.env.srcdir))

        for line in self.content:
            if not line.strip() or self.content.index(line) == len(self.content) - 1:
                continue

            # Adjust the path if it's not absolute
            image_path = line.strip()
            if not image_path.startswith('/'):
                image_path = os.path.join(doc_dir, image_path)
                
            # Make path relative to source directory
            rel_path = os.path.relpath(image_path, self.env.srcdir)

            # Ensure the URI is correct for the environment
            image_node = nodes.image(uri=rel_path)
            figure_node += image_node

        # The last line of the content is treated as the caption
        caption_text = self.content[-1].strip()
        figure_node += nodes.caption('', caption_text)

        return [figure_node]

def setup(app):
    app.add_directive("multiimagefigure", MultiImageFigure)
