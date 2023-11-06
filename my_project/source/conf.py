# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# ajouter le dossier de nos modules
import os
import sys
print(os.getcwd())
sys.path.insert(0, os.path.abspath('../genomic/'))


project = 'DocuTP2'
copyright = '2023, Jonas Meziane'
author = 'Jonas Meziane'
release = 'v1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Configuration de sphinx autodoc
extensions = ['sphinx.ext.autodoc']
exclude_patterns = ['.ipynb_checkpoints']

templates_path = ['_templates']

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
