Plone-Nutzerhandbuch
====================

.. badges::

Status
------

.. image:: https://img.shields.io/github/contributors/veit/plone-nutzerhandbuch.svg
   :alt: Contributors
   :target: https://github.com/veit/plone-nutzerhandbuch/graphs/contributors
.. image:: https://img.shields.io/github/license/veit/plone-nutzerhandbuch.svg
   :alt: License
   :target: https://github.com/veit/plone-nutzerhandbuch/blob/main/LICENSE

.. first-steps::

Installation
------------

#. Download and unpack:

   .. code-block:: console

    $ curl -O https://codeload.github.com/veit/plone-nutzerhandbuch/zip/main
    $ unzip main
    Archive:  main
    …
       creating: plone-nutzerhandbuch-main/
    …

#. Install Pipenv

   Refer to `uv installation
   <https://python-basics-tutorial.readthedocs.io/en/latest/libs/install.html#installation>`_

#. Install Python packages:

   .. code-block:: console

    $ cd plone-nutzerhandbuch-main
    $ uv sync
    $ uv run python -m sphinx -b html docs/ docs/_build/html/

#. Create HTML documentation:

   Note that pandoc has to be installed. On Debian/Ubuntu you can just run

   .. code-block:: console

    $  sudo apt-get install pandoc

    To create the HTML documentation run these commands:

   .. code-block:: console

    $ python3 -m venv .
    $ bin/python -m pip install --upgrade pip
    $ bin/python -m pip install -r docs/constraints.txt
    $ bin/sphinx-build -ab html docs/ docs/_build/

#. Create a PDF:

   For the creation of a PDF file you need additional packages.

   For Debian/Ubuntu you get them with the following command:

   .. code-block:: console

    $ sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

   or for macOS with:

   .. code-block:: console

    $ brew cask install mactex
    …
    🍺  mactex was successfully installed!
    $ curl --remote-name https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
    $ sudo texlua install-getnonfreefonts
    …
    mktexlsr: Updating /usr/local/texlive/2020/texmf-dist/ls-R...
    mktexlsr: Done.

   Then you can generate a PDF with:

   .. code-block:: console

    $ cd docs/
    $ uv run make latexpdf
    …
    The LaTeX files are in _build/latex.
    Run 'make' in that directory to run these through (pdf)latex
    …

   You can find the PDF at ``docs/_build/latex/plone-entwicklerhandbuch.pdf``.

#. Install vnd run ale to check spelling

   You can install Vale with:

   .. code-block:: console

    $ brew install vale

   You can install the parser for Restructuredtext with:

   .. code-block:: console

    $ brew install docutils

   .. seealso::
      * `Vale installation <https://docs.errata.ai/vale/install>`_
      * `Vale formats <https://docs.errata.ai/vale/scoping#formats>`_

   Now you can check the RestructuredText files with:

   .. code-block:: console

    $ cdplone-nutzerhandbuch
    $ vale docs/
    ✔ 0 errors, 0 warnings and 0 suggestions in 201 files.

Pull-Requests
-------------

If you have suggestions for improvements and additions, I recommend that you
create a `Fork <https://github.com/veit/plone-nutzerhandbuch/fork>`_ of my
`GitHub Repository <https://github.com/veit/plone-nutzerhandbuch/>`_ and make
your changes there. You are also welcome to make a *pull request*. If the
changes contained therein are small and atomic, I’ll be happy to look at your
suggestions.
