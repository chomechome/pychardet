# Fast universal encoding detection in Python
This library is a python binding to [universal chardet](https://github.com/BYVoid/uchardet).
## Example
### Python 3
```python
>>> from pychardet import detect_encoding
>>> encoded = 'El español o castellano es una lengua romance procedente del latín hablado'.encode('iso-8859-1')
>>> detect_encoding(encoded)
Encoding(name=<EncodingName.ISO_8859_1: 'iso-8859-1'>, confidence=0.835808515548706)
```
### Python 2
```python
>>> from pychardet import detect_encoding
>>> encoded = u'El español o castellano es una lengua romance procedente del latín hablado'.encode('iso-8859-1')
>>> detect_encoding(encoded)
Encoding(name=<EncodingName.ISO_8859_1: 'iso-8859-1'>, confidence=0.835808515548706)
```
## Installation

### Requirements
[Cython](http://docs.cython.org/src/quickstart/install.html) >= 0.24

### From PyPI
```bash
$ pip install pychardet
```
