from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

tools_dir = './src/'

setup(
    ext_modules=cythonize(
        Extension('trie',
                  sources=['trie.pyx'],
                  include_dirs=[tools_dir],
                  language='c++')
    ))
