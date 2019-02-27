from distutils.core import setup

setup(
    name='dumbhost',
    version='0.1',
#    py_modules=[
#        'sendmail',
#    ],
    packages = ['dumbhost'],
    scripts = ['sendmail'],
    data_files = [
        ('/etc', ['dumbhost.conf']),
        ('/etc', ['dumbhost.license']),
    ],
    description='simple mailer for satellite hosts',
    author = 'Sergey Dorofeev',
    author_email = 'sergey@fidoman.ru',
    url = 'http://sergey.fidoman.ru/code/dumbhost/',
    license = 'MIT',
)
