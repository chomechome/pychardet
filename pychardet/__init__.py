import enum
from typing import NamedTuple, Optional

from pychardet.encoding_detector import EncodingDetector

__name__ = "pychardet"
__version__ = "0.0.7"


Encoding = NamedTuple("Encoding", [("name", Optional[str]), ("confidence", float)])


@enum.unique
class EncodingName(str, enum.Enum):
    ASCII = "ascii"
    BIG5 = "big5"
    EUC_JP = "euc-jp"
    EUC_KR = "euc-kr"
    EUC_TW = "euc-tw"
    GB18030 = "gb18030"
    HZ_GB_2312 = "hz-gb-2312"
    IBM852 = "ibm852"
    IBM855 = "ibm855"
    IBM866 = "ibm866"
    ISO_2022_CN = "iso-2022-cn"
    ISO_2022_JP = "iso-2022-jp"
    ISO_2022_KR = "iso-2022-kr"
    ISO_8859_1 = "iso-8859-1"
    ISO_8859_10 = "iso-8859-10"
    ISO_8859_11 = "iso-8859-11"
    ISO_8859_13 = "iso-8859-13"
    ISO_8859_15 = "iso-8859-15"
    ISO_8859_16 = "iso-8859-16"
    ISO_8859_2 = "iso-8859-2"
    ISO_8859_3 = "iso-8859-3"
    ISO_8859_4 = "iso-8859-4"
    ISO_8859_5 = "iso-8859-5"
    ISO_8859_6 = "iso-8859-6"
    ISO_8859_7 = "iso-8859-7"
    ISO_8859_8 = "iso-8859-8"
    ISO_8859_9 = "iso-8859-9"
    KOI8_R = "koi8-r"
    MAC_CENTRAL_EUROPE = "maccentraleurope"
    MAC_CYRILLIC = "maccyrillic"
    SHIFT_JIS = "shift_jis"
    TIS_620 = "tis-620"
    UHC = "uhc"
    UTF_16 = "utf-16"
    UTF_16BE = "utf-16be"
    UTF_16LE = "utf-16le"
    UTF_32 = "utf-32"
    UTF_32BE = "utf-32be"
    UTF_32LE = "utf-32le"
    UTF_8 = "utf-8"
    VISCII = "viscii"
    WINDOWS_1250 = "windows-1250"
    WINDOWS_1251 = "windows-1251"
    WINDOWS_1252 = "windows-1252"
    WINDOWS_1253 = "windows-1253"
    WINDOWS_1255 = "windows-1255"
    WINDOWS_1256 = "windows-1256"
    WINDOWS_1257 = "windows-1257"
    WINDOWS_1258 = "windows-1258"
    X_ISO_10646_UCS_4_21431 = "x-iso-10646-ucs-4-21431"
    X_ISO_10646_UCS_4_34121 = "x-iso-10646-ucs-4-34121"

    @classmethod
    def _missing_(cls, value: str):
        aliases = {
            "mac-cyrillic": EncodingName.MAC_CYRILLIC,
            "mac-centraleurope": EncodingName.MAC_CENTRAL_EUROPE,
        }
        if value in aliases:
            return aliases[value]
        return super()._missing_(value)


def detect_encoding(byte_str: bytes) -> Encoding:
    with EncodingDetector() as detector:
        detector.feed(byte_str)
        encoding, confidence = detector.result
        if encoding is None:
            return Encoding(name=None, confidence=confidence)
        return Encoding(name=EncodingName(encoding), confidence=confidence)
