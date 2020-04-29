import os
import pathlib

import pytest

from pychardet import EncodingName, detect_encoding
from tests.utils import skip

_DIRECTORY = pathlib.Path(__file__).absolute().parent


def _get_stemmed_basename(path):
    return os.path.splitext(os.path.basename(path))[0]


def _get_test_files():
    path = _DIRECTORY / '..' / 'pychardet' / 'uchardet' / 'test'
    return path.glob('*/*.txt')


def _mark_known_failures(path: pathlib.Path):
    encoding = path.stem
    for failure in [
        '/test/he/iso-8859-8.txt',
        '/test/da/iso-8859-1.txt',
        '/test/ja/utf-16le.txt',
        '/test/ja/utf-16be.txt',
        '/test/es/iso-8859-15.txt',
    ]:
        if str(path).endswith(failure):
            return skip(path, encoding, reason='Fails in uchardet')
    return path, encoding


@pytest.mark.parametrize(
    ('path', 'encoding'),
    [_mark_known_failures(path) for path in _get_test_files()],
)
def test_detect_on_files(path, encoding):
    with path.open('rb') as file:
        text = file.read()

    assert detect_encoding(text).name == EncodingName(encoding)


@pytest.mark.parametrize(
    ('text', 'encoding'),
    [
        ('русский', EncodingName.UTF_8),
        ('français', EncodingName.UTF_16),
        ('español', EncodingName.UTF_32),
    ]
)
def test_detect_on_text(text, encoding):
    assert detect_encoding(text.encode(encoding)).name == encoding
