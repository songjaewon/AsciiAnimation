#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Asciimation created by Jaewon Song.
#  Distributed under the terms of the new BSD license.
# -----------------------------------------------------------------------------
from os import path
from codecs import open
from setuptools import setup, Extension

description = """
Asciimation for Python script
==============================

Asciimation creating

Installation
============

To be able to use freetype python, you need the freetype library version 2
installed on your system.

Mac users
---------

Freetype should be already installed on your system. If not, either install it
using `homebrew <http://brew.sh>`_ or compile it and place the library binary
file in '/usr/local/lib'.

Linux users
-----------

Freetype should be already installed on your system. If not, either install
relevant package from your package manager or compile from sources and place
the library binary file in '/usr/local/lib'.

Window users
------------

You can try to install a window binaries available from the Freetype site or
you can compile it from sources. In such a case, make sure the resulting
library binaries is named 'Freetype.dll' (and not something like
Freetype245.dll) and make sure to place a copy in Windows/System32 directory.

Usage example
=============

.. code:: python

   import freetype
   face = freetype.Face("Vera.ttf")
   face.set_char_size( 48*64 )
   face.load_char('S')
   bitmap = face.glyph.bitmap
   print bitmap.buffer

Contributors
============

* Titusz Pan (bug report)
* Ekkehard.Blanz (bug report)
* Jānis Lībeks (bug report)
* Frantisek Malina (typo)
* Tillmann Karras (bug report & fix)
* Matthew Sitton (bug report & fix)
* Tao Gong (bug report)
* Matthew Sitton (Remove raw interfaces from the __init__.py file)
"""

setup( name        = 'Asciimation',
       version     = '1.0.1',
       description = 'Asciimation python bindings',
       long_description = description,
       author      = 'Jaewon Song',
       author_email= 'songjaewon@kaist.ac.kr',
       url         = 'https://github.com/songjaewon/AsciiAnimation',
       packages    = ['DocuTest'],
       classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Environment :: X11 Applications',
          'Environment :: MacOS X',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Multimedia :: Graphics',
          ],
     )
