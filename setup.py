from distutils.core import setup

setup(
    name='FlexDoIT',
    version='0.1',
    author='Bruce Zhang',
    author_email='flexdoit@gmail.com',
    scripts=['flexdoit'],
    url='https://github.com/flexdoit/flexdoit',
    description='For IT engineer',
    install_requires=[
        "ansible >= 1.3"
    ],
)
