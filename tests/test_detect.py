# coding=utf-8
import glob
import os

import pytest

from pychardet import detect_encoding, EncodingName
from tests.utils import skip

_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def _get_stemmed_basename(path):
    return os.path.splitext(os.path.basename(path))[0]


def _get_test_files():
    return glob.glob(
        os.path.normpath(
            os.path.join(_DIRECTORY, "../pychardet/uchardet/test/*/*.txt")
        )
    )


def _mark_known_failures(path):
    encoding = _get_stemmed_basename(path)
    for failure in [
        "/test/he/iso-8859-8.txt",
        "/test/da/iso-8859-1.txt",
        "/test/ja/utf-16le.txt",
        "/test/ja/utf-16be.txt",
        "/test/es/iso-8859-15.txt",
    ]:
        if path.endswith(failure):
            return skip(path, encoding, reason="Fails in uchardet")
    return path, encoding


@pytest.mark.parametrize(
    ("path", "encoding"),
    [_mark_known_failures(path) for path in _get_test_files()],
)
def test_detect_encoding(path, encoding):
    with open(path, "rb") as f:
        text = f.read()

    assert detect_encoding(text).name == EncodingName(encoding)
