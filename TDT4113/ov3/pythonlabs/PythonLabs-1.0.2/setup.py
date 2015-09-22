from distutils.core import setup

setup(
    name = 'PythonLabs',
    version = '1.0.2',
    author = 'John Conery',
    author_email = 'conery@uoregon.edu',
    packages = ['PythonLabs'],
    package_data = {'': [
        'data/eliza/*.txt',
        'data/email/*.txt',
        'data/huffman/*.txt',
        'data/life/*.txt',
        'data/mars/*.txt',
        'data/spheres/*.txt',
        'data/testsets/*.txt',
        'data/text/*.txt',
        'data/tsp/*.txt'
    ]},
    # scripts = ['bin/...', 'bin/...'],
    url = 'http://www.cs.uoregon.edu/eic',
    license = 'LICENSE.txt',
    description = 'Lab modules for the textbook Explorations in Computing (Python edition)',
    long_description = open('README.txt').read(),
)
