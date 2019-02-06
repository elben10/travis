from setuptools import setup, find_packages

def parse_requirements(requirements, ignore=('setuptools',)):
    """
    Read dependencies from requirements file (with version numbers if any)
    Notes:
        - this implementation does not support requirements files with extra
          requirements
        - this implementation has been taken from TailorDev/Watson's setup file
    """
with open(requirements) as f:
    packages = set()
    for line in f:
        line = line.strip()
        if line.startswith(('#', '-r', '--')):
            continue
        if '#egg=' in line:
            line = line.split('#egg=')[1]
        pkg = line.strip()
        if pkg not in ignore:
            packages.add(pkg)
    return list(packages)

setup(
    name = 'MyPackageName',
    version = '1.0.0',
    url = 'https://github.com/mypackage.git',
    author = 'Author Name',
    author_email = 'author@gmail.com',
    description = 'Description of my package',
    packages = find_packages(),    
    install_requires=parse_requirements('requirements.txt'),
    setup_requires=['pytest-runner', ],
    tests_require=parse_requirements('requirements-dev.txt'),
)
