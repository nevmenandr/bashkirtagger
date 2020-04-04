from setuptools import setup

def long_desc():
    with open('README.rst', 'r', encoding='utf-8') as f:
        return f.read()

setup(name='bashkirtagger',
      version='0.7.1',
      description='Utility for part-of-speech tagging of Bashkir text',
      long_description=long_desc(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
        'Intended Audience :: Developers'
      ],
      author='Boris Orekhov',
      license="GPL",
      keywords='nlp bashkir pos tagger',
      author_email='nevmenandr@gmail.com',
      url='https://github.com/nevmenandr/bashkirtagger',
      packages=['bashkirtagger'],
      install_requires=[
          'requests',
          'Keras',
          'numpy',
          'tensorflow'
      ],
      include_package_data=True,
      zip_safe=False)