#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

#
# PyTorch documentation build configuration file, created by
# sphinx-quickstart on Fri Dec 23 13:31:47 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import subprocess
import sys

import pytorch_sphinx_theme
from docutils import nodes
from sphinx import addnodes
from sphinx.util.docfields import TypedField

sys.path.append(os.path.abspath("./ext"))

if True:  # stop isort from reordering
    sys.path.append(os.path.abspath("../.."))
    import torchx

FBCODE = "fbcode" in os.getcwd()

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "1.6"

user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0 github.com/pytorch/torchx"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    "compatibility",
    "runopts",
    "fbcode",
    "nbsphinx",
    "IPython.sphinxext.ipython_console_highlighting",
]
if not FBCODE:
    extensions += [
        "sphinx.ext.intersphinx",
        "sphinxcontrib.katex",
        "sphinx_gallery.gen_gallery",
    ]

if FBCODE:
    nbsphinx_execute = "never"

html_context = {"fbcode": FBCODE}

# coverage options

coverage_ignore_modules = [
    "torchx.components.component_test_base",
]

# katex options
#
#

katex_options = r"""
delimiters : [
   {left: "$$", right: "$$", display: true},
   {left: "\\(", right: "\\)", display: false},
   {left: "\\[", right: "\\]", display: true}
]
"""

napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "PyTorch/TorchX"
copyright = "2020, TorchX Contributors"
author = "TorchX Contributors"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# TODO: change to [:2] at v1.0
version = f"v{torchx.__version__}"
# The full version, including alpha/beta/rc tags.
# TODO: verify this works as expected
release = "main"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "examples_*/**/*.ipynb",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pytorch_sphinx_theme"
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "pytorch_project": "torchx",
    "collapse_navigation": False,
    "display_version": True,
    "logo_only": True,
    "analytics_id": "UA-117752657-2",
}

html_logo = "_static/img/pytorch-logo-dark.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


html_css_files = [
    "https://cdn.jsdelivr.net/npm/katex@0.10.0-beta/dist/katex.min.css",
    "css/torchx.css",
]
html_js_files = [
    "js/torchx.js",
]


def setup(app):
    # NOTE: in Sphinx 1.8+ `html_css_files` is an official configuration value
    # and can be moved outside of this function (and the setup(app) function
    # can be deleted).

    # In Sphinx 1.8 it was renamed to `add_css_file`, 1.7 and prior it is
    # `add_stylesheet` (deprecated in 1.8).
    add_css = getattr(
        app, "add_css_file", getattr(app, "add_stylesheet", None)
    )  # noqa B009
    for css_file in html_css_files:
        add_css(css_file)


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "TorchXdoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "pytorch.tex",
        "TorchX Documentation",
        "Torch Contributors",
        "manual",
    )
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "TorchX", "TorchX Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "TorchX",
        "TorchX Documentation",
        author,
        "TorchX",
        "TorcheXtended",
        "Miscellaneous",
    )
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
}

# -- A patch that prevents Sphinx from cross-referencing ivar tags -------
# See http://stackoverflow.com/a/41184353/3343043


def patched_make_field(self, types, domain, items, **kw):
    # `kw` catches `env=None` needed for newer sphinx while maintaining
    #  backwards compatibility when passed along further down!

    def handle_item(fieldarg, content):
        par = nodes.paragraph()
        par += addnodes.literal_strong("", fieldarg)  # Patch: this line added
        # par.extend(self.make_xrefs(self.rolename, domain, fieldarg,
        #                           addnodes.literal_strong))
        if fieldarg in types:
            par += nodes.Text(" (")
            # NOTE: using .pop() here to prevent a single type node to be
            # inserted twice into the doctree, which leads to
            # inconsistencies later when references are resolved
            fieldtype = types.pop(fieldarg)
            if len(fieldtype) == 1 and isinstance(fieldtype[0], nodes.Text):
                typename = "".join(n.astext() for n in fieldtype)
                typename = typename.replace("int", "python:int")
                typename = typename.replace("long", "python:long")
                typename = typename.replace("float", "python:float")
                typename = typename.replace("type", "python:type")
                par.extend(
                    self.make_xrefs(
                        self.typerolename,
                        domain,
                        typename,
                        addnodes.literal_emphasis,
                        **kw,
                    )
                )
            else:
                par += fieldtype
            par += nodes.Text(")")
        par += nodes.Text(" -- ")
        par += content
        return par

    fieldname = nodes.field_name("", self.label)
    if len(items) == 1 and self.can_collapse:
        fieldarg, content = items[0]
        bodynode = handle_item(fieldarg, content)
    else:
        bodynode = self.list_type()
        for fieldarg, content in items:
            bodynode += nodes.list_item("", handle_item(fieldarg, content))
    fieldbody = nodes.field_body("", bodynode)
    return nodes.field("", fieldname, fieldbody)


TypedField.make_field = patched_make_field


# -- Options for Sphinx-Gallery -----

if FBCODE:
    tags = []
else:
    tags_raw = subprocess.check_output(["git", "tag", "-l"])
    tags = set(tags_raw.decode("utf-8").strip().split("\n"))

if version in tags:
    notebook_version = version
    code_url = (
        f"https://github.com/pytorch/torchx/archive/refs/tags/{notebook_version}.tar.gz"
    )
else:
    notebook_version = "main"
    code_url = f"https://github.com/pytorch/torchx/archive/refs/heads/{notebook_version}.tar.gz"

first_notebook_cell = f"""
!pip install torchx[kfp]
!wget --no-clobber {code_url}
!tar xf {notebook_version}.tar.gz --strip-components=1

NOTEBOOK = True
""".strip()

sphinx_gallery_conf = {
    "examples_dirs": [
        "../../torchx/examples/apps",
        "../../torchx/examples/pipelines",
    ],
    "gallery_dirs": [
        "examples_apps",
        "examples_pipelines",
    ],
    "first_notebook_cell": first_notebook_cell,
}

# -- Options for autosectionlabel

# add the document to avoid collisions for common titles
autosectionlabel_prefix_document = True


# Options for nbsphinx

nbsphinx_custom_formats = {
    ".md": ["jupytext.reads", {"fmt": "markdown"}],
}
nbsphinx_epilog = r"""
.. raw:: html

    <div id="is-nbsphinx"></div>
"""

nbsphinx_requirejs_path = ""

if os.environ.get("SKIP_NB"):
    nbsphinx_execute = "never"
