# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'MaskGraphene'
copyright = '2024, Yunfei Hu'
author = 'Yunfei Hu'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration

extensions = [
    "nbsphinx",
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

nbsphinx_allow_errors = True
