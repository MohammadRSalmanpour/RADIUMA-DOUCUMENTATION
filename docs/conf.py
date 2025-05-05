extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinx.ext.imgmath',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add configuration for static files
html_static_path = ['_static']

# Set the master document
master_doc = 'index'

# Enable nitpicky mode to catch all references issues
nitpicky = True

# Debug options
keep_warnings = True
