# Configuration file for the Sphinx documentation builder.

import os 
import sys

#For real idk what the fuck is going on im just trying wrong paths since nothing does work

sys.path.insert(0, os.path.abspath('../..'))

# -- AutoAPI configuration settings
# autoapi_dirs = ['../../']
# autoapi_generate_api_docs = False
# -- Project information
project = 'PySpace'
copyright = '2022, Capernicus'
author = 'Capernicus'

release = '1.0'
version = '1.5.0'
#Enable hoverxref 
hoverxref_sphinxtabs = True
extensions = [
    'sphinx.ext.autodoc',
    'karma_sphinx_theme',
    'sphinx.ext.napoleon',
]


# -- Options for HTML output

html_theme = 'karma_sphinx_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
