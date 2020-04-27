# coding=utf-8
import pytest
import six

from pychardet import EncodingDetector, EncodingName


@pytest.fixture()
def detector():
    return EncodingDetector()


@pytest.fixture(scope="session")
def unicode_text():
    return six.text_type("Encodings are fun!")


@pytest.fixture(scope="session")
def ascii_text(unicode_text):
    return unicode_text.encode(EncodingName.ASCII)


def test_feed(detector, ascii_text):
    detector.feed(ascii_text)

    assert detector.is_done
    assert detector.result == (EncodingName.ASCII, 1.0)


def test_feed_unicode(detector, unicode_text):
    with pytest.raises(TypeError):
        detector.feed(unicode_text)


def test_close(detector, ascii_text):
    detector.feed(ascii_text)
    detector.close()

    assert not detector.is_done
    assert detector.result == (None, 0.0)


def test_with_statement_closes_detector(detector, ascii_text):
    with detector:
        detector.feed(ascii_text)

    assert not detector.is_done
    assert detector.result == (None, 0.0)
