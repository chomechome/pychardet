import glob

from Cython.Distutils import build_ext
from setuptools import Extension


def get_extensions():
    lang_models = glob.glob("pychardet/uchardet/src/LangModels/*.cpp")
    uchardet_sources = glob.glob("pychardet/uchardet/src/*.cpp")
    pychardet_sources = [
        "pychardet/encoding_detector.pyx",
        "pychardet/detector.cpp",
    ]
    return [
        Extension(
            "pychardet.encoding_detector",
            sources=pychardet_sources + uchardet_sources + lang_models,
            language="c++",
        )
    ]


def build(setup_kwargs):
    setup_kwargs.update(
        {"ext_modules": get_extensions(), "cmdclass": {"build_ext": build_ext}}
    )
