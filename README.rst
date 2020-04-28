Fast universal encoding detection in Python
===========================================


.. image:: https://img.shields.io/pypi/v/pychardet.svg
    :target: https://pypi.python.org/pypi/pychardet
    :alt: Package version

.. image:: https://img.shields.io/pypi/l/pychardet.svg
    :target: https://pypi.python.org/pypi/pychardet
    :alt: Package license

.. image:: https://img.shields.io/pypi/pyversions/pycardet.svg
    :target: https://pypi.python.org/pypi/pychardet
    :alt: Python versions

.. image:: https://travis-ci.org/chomechome/pychardet.svg?branch=master
    :target: https://travis-ci.org/chomechome/pychardet
    :alt: TravisCI status


---------------

**pychardet** is a Python binding to [uchardet](https://gitlab.freedesktop.org/uchardet/uchardet) - fast universal character encoding detection library.


Installation
------------

::

    $ pip install pychardet


Example
-------

.. code-block:: python

    >>> from pychardet import detect_encoding
    >>> encoded = 'El español o castellano es una lengua romance procedente del latín hablado'.encode('iso-8859-1')
    >>> detect_encoding(encoded)
    Encoding(name=<EncodingName.ISO_8859_1: 'iso-8859-1'>, confidence=0.835808515548706)
