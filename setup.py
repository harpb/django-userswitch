from distutils.core import setup

setup(
    name = "django-userswitch",
    version = "0.1a",
    packages = ['userswitch',],
    license = "New BSD License",
    author = open('AUTHORS.rst').read(),
    author_email = "hello@ikraftsoft.com",
    description = "A quick 'n' dirty Django app for switching between different users while testing",
    url = "https://github.com/ikraftsoft/django-userswitch",
    include_package_data=True,
)
