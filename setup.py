'''Setup Script for package.'''
from distutils.core import setup

setup(name='Duplicate Files Checker',
      version='1.0',
      description='Checks the duplicates file in the system.',
      author='Arjun Adhikari',
      author_email='arjunadhikari@protonmail.com',
      url='https://github.com/theArjun/duplicate-files-checker',
      packages=['creator'],
      classifiers=[
          'Development Status :: 1 Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development :: Version Control',
      ],
      )

if __name__ == "__main__":
    setup()
