# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

### these imports are need for support for custom css file
from docutils.parsers.rst import roles
from docutils import nodes


# -- Project information -----------------------------------------------------

project = 'CXLS Interlock System Documentation'
copyright = '2024, Eric Everett'
author = 'Eric Everett'

# The full version, including alpha/beta/rc tags
release = '2024'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.duration'] ### Added extension

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

pygments_style = 'sphinx' ### Added style

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme' ### Changed theme to alabaster

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['custom.css'] ### Added custom css file

# Pygments (syntax highlighting) style to use
pygments_style = 'friendly' ### Added style

# This is the correct place for html_add_permalinks configuration
html_permalinks = False  ### Disable ¶ symbols next to headings

# -- added definitions for custom roles --------------------------------------

def colored_text(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """ This function is used to add colored text into the documentation.

    Args:
        name (_type_): _description_
        rawtext (_type_): _description_
        text (_type_): _description_
        lineno (_type_): _description_
        inliner (_type_): _description_
        options (dict, optional): _description_. Defaults to {}.
        content (list, optional): _description_. Defaults to [].

    Returns:
        _type_: _description_
    """
    
    node = nodes.inline(rawtext, text, classes=[name])
    return [node], []

roles.register_local_role('red', colored_text)
roles.register_local_role('green', colored_text) 



def colored_cell_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    
    """ This function is used to add colored cells to tabels.

    Returns:
        _type_: _description_
    """
    
    node = nodes.inline(rawtext, text, classes=[role])
    return [node], []

roles.register_local_role('red-cell', colored_cell_role)
roles.register_local_role('blue-cell', colored_cell_role)



def subscript_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """This function is used to add subscript text into the documentation.

    Args:
        name (_type_): _description_
        rawtext (_type_): _description_
        text (_type_): _description_
        lineno (_type_): _description_
        inliner (_type_): _description_
        options (dict, optional): _description_. Defaults to {}.
        content (list, optional): _description_. Defaults to [].

    Returns:
        _type_: _description_
    """
    node = nodes.subscript(rawtext, text, classes=[name])
    return [node], []

roles.register_local_role('sub', subscript_role)