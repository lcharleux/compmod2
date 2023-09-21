from setuptools import setup

setup(name='compmod2',
      version='0.1',
      description="Compartmentalized models with Argiope",
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
          "pandas",
          "argiope",
          ],
      package_data={'compmod2': ['templates\models\RVETest\*.inp', 'templates\models\RVETest\*.py']},
      include_package_data=True,
      )
