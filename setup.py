from setuptools import setup

setup(name='compmod2',
      version='0.0',
      description="Compartmentalized models",
      long_description="",
      author='Ludovic Charleux',
      author_email='ludovic.charleux@univ-smb.fr',
      license='GPL v3',
      packages=['compmod2'],
      zip_safe=False,
      install_requires=[
          "numpy",
          "scipy",
          "matplotlib",
          "pandas"
          "argiope"
          ],
      )
