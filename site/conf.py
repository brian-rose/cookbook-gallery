#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
import os
import shutil
import sys

sys.path.insert(0, os.path.abspath("_extensions"))


# -- Project information -----------------------------------------------------

project = "Project Pythia Cookbooks"
author = 'the <a href="https://projectpythia.org/">Project Pythia</a> Community'
copyright = "2024"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_design",
    "cookbook_gallery_generator",
]

# Define what extensions will parse which kind of source file
source_suffix = {
    ".ipynb": "myst-nb",
    ".myst": "myst-nb",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_pythia_theme"
html_last_updated_fmt = "%-d %B %Y"

# Logo & Title
html_logo = "_static/images/logos/pythia_logo-white-rtext.svg"
html_title = ""

# Favicon
html_favicon = "_static/images/icons/favicon.ico"

# Permalinks Icon
html_permalinks_icon = '<i class="fas fa-link"></i>'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]
# html_js_files = ['custom.js']

# Disable Sidebars on special pages
html_sidebars = {
    "index": [],
}

# HTML Theme-specific Options
html_theme_options = {
    'analytics': {
            'google_analytics_id': 'G-T52X8HNYE8',
        },
    "github_url": "https://github.com/ProjectPythia",
    "twitter_url": "https://twitter.com/project_pythia",
    "icon_links": [
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/channel/UCoZPBqJal5uKpO8ZiwzavCw",
            "icon": "fab fa-youtube-square",
            "type": "fontawesome",
        }
    ],
    'logo': {
            'link': 'https://projectpythia.org',
    },
    'navbar_align': 'left',
    'navbar_start': ['navbar-logo'],
    "navbar_links": [
        {"name": "Home", "url": "https://projectpythia.org"},
        {"name": "Foundations", "url": "https://foundations.projectpythia.org"},
        {"name": "Cookbooks", "url": "https://cookbooks.projectpythia.org/"},
        {"name": "Resources", "url": "https://projectpythia.org/resource-gallery.html"},
        {"name": "Community", "url": "https://projectpythia.org/#join-us"},
        {"name": "Blog", "url": "https://projectpythia.org/blog.html"},
    ],
    'navbar_end': ['navbar-icon-links'],
    "page_layouts": {
        "index": "page-standalone.html",
    },
    'secondary_sidebar_items': [],
    "footer_logos": {
        "NCAR": "_static/images/logos/NSF-NCAR_Lockup-UCAR-Dark_102523.svg",
        "Unidata": "_static/images/logos/Unidata_logo_horizontal_1200x300.svg",
        "UAlbany": "_static/images/logos/UAlbany-A2-logo-purple-gold.svg",
    },
    'footer_start': ['footer-logos', 'footer-menu', 'footer-info', 'footer-extra'],
}

# MyST config
myst_enable_extensions = ["amsmath", "colon_fence", "deflist", "html_image"]
myst_url_schemes = ["http", "https", "mailto"]
nb_execution_mode = 'off'
myst_heading_anchors = 3

# Don't run the link checker on immutable DOI links
linkcheck_ignore = ['https://doi.org/*']

# CUSTOM SCRIPTS ==============================================================
