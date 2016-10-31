from setuptools import setup
setup(
  name='chatfirst',
  version='0.1.0',
  description='Chatfirst Python Client',
  long_description=open('README.md').read(),
  author='Ivan Tertychnyy',
  author_email='it@chatfirst.co',
  packages=['chatfirst'],
  url='https://github.com/chatfirst/chatfirst',
  download_url='https://github.com/chatfirst/chatfirst/tarball/v0.1.0',
  license='LICENSE.txt',
  install_requires=[
        "requests>=2.10.0",
    ],
)
