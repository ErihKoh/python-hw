from setuptools import setup, find_packages

setup(
    name='cli_assistant',
    version='1',
    description='Script help you working with contacts, notes and help you sort files in folder',
    packages=find_packages(),
    requires=['fuzzywuzzy'],
    entry_points={'console_scripts': ['smart = cli_assistant.app:main']}
)