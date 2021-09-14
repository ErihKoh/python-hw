from setuptools import setup

setup(
    name='clean_folder',
    description='App for sort and clean folder',
    url='https://github.com/ErihKoh/hw-7-package',
    author='ErihKoh',
    author_email='barsuk0831@gmail.com',
    license='MIT',
    packages=['clean_folder'],
    entry_points={'console_scripts': ['cleanf = clean_folder.clean:main']}
)