===========================================
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

**pychardet** is a Python binding to `uchardet <https://gitlab.freedesktop.org/uchardet/uchardet>`_ - fast universal character encoding detection library.


------------
Installation
------------

::

    $ pip install Cython==0.24
    $ pip install pychardet


-------
Example
-------

.. code-block:: python

    >>> from pychardet import detect_encoding
    >>> encoded = b'El espa\xf1ol o castellano es una lengua romance procedente del lat\xedn hablado'
    >>> encoding = detect_encoding(encoded)
    >>> encoding
    Encoding(name=<EncodingName.ISO_8859_1: 'iso-8859-1'>, confidence=0.835808515548706)
    >>> encoded.decode(encoding.name)
    'El español o castellano es una lengua romance procedente del latín hablado'

-------------------
Supported Encodings
-------------------

- International (Unicode)
    * UTF-8
    * UTF-16 / UTF-16BE / UTF-16LE
    * UTF-32 / UTF-32BE / UTF-32LE
    * X-ISO-10646-UCS-4-34121 / X-ISO-10646-UCS-4-21431 [1]_
- Arabic
    * ISO-8859-6
    * WINDOWS-1256
- Bulgarian
    * ISO-8859-5
    * WINDOWS-1251
- Chinese
    * ISO-2022-CN [1]_
    * BIG5
    * EUC-TW [1]_
    * GB18030
    * HZ-GB-2312
- Croatian:
    * ISO-8859-2
    * ISO-8859-13
    * ISO-8859-16
    * Windows-1250
    * IBM852
    * MAC-CENTRALEUROPE
- Czech
    * Windows-1250
    * ISO-8859-2
    * IBM852
    * MAC-CENTRALEUROPE
- Danish
    * ISO-8859-1
    * ISO-8859-15
    * WINDOWS-1252
- English
    * ASCII
- Esperanto
    * ISO-8859-3
- Estonian
    * ISO-8859-4
    * ISO-8859-13
    * ISO-8859-13
    * Windows-1252
    * Windows-1257
- Finnish
    * ISO-8859-1
    * ISO-8859-4
    * ISO-8859-9
    * ISO-8859-13
    * ISO-8859-15
    * WINDOWS-1252
- French
    * ISO-8859-1
    * ISO-8859-15
    * WINDOWS-1252
- German
    * ISO-8859-1
    * WINDOWS-1252
- Greek
    * ISO-8859-7
    * WINDOWS-1253
- Hebrew
    * ISO-8859-8
    * WINDOWS-1255
- Hungarian:
    * ISO-8859-2
    * WINDOWS-1250
- Irish Gaelic
    * ISO-8859-1
    * ISO-8859-9
    * ISO-8859-15
    * WINDOWS-1252
- Italian
    * ISO-8859-1
    * ISO-8859-3
    * ISO-8859-9
    * ISO-8859-15
    * WINDOWS-1252
- Japanese
    * ISO-2022-JP
    * SHIFT_JIS
    * EUC-JP
- Korean
    * ISO-2022-KR
    * EUC-KR / UHC
- Lithuanian
    * ISO-8859-4
    * ISO-8859-10
    * ISO-8859-13
- Latvian
    * ISO-8859-4
    * ISO-8859-10
    * ISO-8859-13
- Maltese
    * ISO-8859-3
- Polish:
    * ISO-8859-2
    * ISO-8859-13
    * ISO-8859-16
    * Windows-1250
    * IBM852
    * MAC-CENTRALEUROPE
- Portuguese
    * ISO-8859-1
    * ISO-8859-9
    * ISO-8859-15
    * WINDOWS-1252
- Romanian:
    * ISO-8859-2
    * ISO-8859-16
    * Windows-1250
    * IBM852
- Russian
    * ISO-8859-5
    * KOI8-R
    * WINDOWS-1251
    * MAC-CYRILLIC
    * IBM866
    * IBM855
- Slovak
    * Windows-1250
    * ISO-8859-2
    * IBM852
    * MAC-CENTRALEUROPE
- Slovene
    * ISO-8859-2
    * ISO-8859-16
    * Windows-1250
    * IBM852
    * MAC-CENTRALEUROPE
- Spanish
    * ISO-8859-1
    * ISO-8859-15
    * WINDOWS-1252
- Swedish
    * ISO-8859-1
    * ISO-8859-4
    * ISO-8859-9
    * ISO-8859-15
    * WINDOWS-1252
- Thai
    * TIS-620
    * ISO-8859-11
- Turkish:
    * ISO-8859-3
    * ISO-8859-9
- Vietnamese:
    * VISCII [1]_
    * Windows-1258
- Others
    * WINDOWS-1252

.. [1] Not supported in Python codecs
