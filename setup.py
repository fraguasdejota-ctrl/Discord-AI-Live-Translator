from setuptools import setup
from Cython.Build import cythonize

setup(
    name="TraductorCore",
    ext_modules=cythonize(
        "traductor_core.py",
        compiler_directives={
            'language_level': "3",
            'always_allow_keywords': True,
            'binding': True  # <-- Vital para PyQt6
        }
    )
)
