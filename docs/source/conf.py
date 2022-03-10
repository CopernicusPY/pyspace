# Configuration file for the Sphinx documentation builder.

import os 
import sys

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

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'karma_sphinx_theme',
    'sphinx.ext.napoleon',
#     'autoapi.extension'

]



# -- Options for HTML output

html_theme = 'karma_sphinx_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
