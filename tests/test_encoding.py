import codecs

import pytest

from pychardet import EncodingName
from tests.utils import skip


def _mark_unsupported(encoding):
    if encoding in [
        EncodingName.EUC_TW,
        EncodingName.ISO_2022_CN,
        EncodingName.VISCII,
        EncodingName.X_ISO_10646_UCS_4_21431,
        EncodingName.X_ISO_10646_UCS_4_34121,
    ]:
        return skip(encoding, reason="Unsupported in Python")
    return encoding


@pytest.mark.parametrize(
    "name", [_mark_unsupported(encoding) for encoding in EncodingName]
)
def test_name_in_codecs(name):
    codecs.lookup(name)
