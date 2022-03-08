# Configuration file for the Sphinx documentation builder.
import sys
import os

sys.path.insert(0, os.path.abspath('../..'))
# -- Project information

project = 'PySpace'
copyright = '2022, Capernicus'
author = 'Capernicus'

release = '0.1'
version = '1.0.0'

# -- General configuration
autosectionlabel_prefix_document = True
hoverxref_auto_ref = True
hoverxref_sphinxtabs = True

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'karma_sphinx_theme',
    'sphinx.ext.napoleon'

]



# -- Options for HTML output

html_theme = 'karma_sphinx_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
