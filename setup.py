from distutils.core import setup

long_description = """Credit Card Validator

A Python program to identify credit card issuer and validate card number using Luhn's algorithm"""

setup(
  name = 'cardvalidate',         # How you named your package folder (MyLib)
  packages = ['cardvalidate'],   # Chose the same as "name"
  version = '0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Credit card number and CVV validator and checker',   # Give a short description about your library
  long_description=long_description,
    long_description_content_type="text/markdown",
  author = 'sawit.tr@gmail.com',                   # Type in your name
  author_email = 'sawit.tr@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/tansawit/cardvalidate',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/tansawit/cardvalidate/archive/0.4.tar.gz',    # I explain this later on
  keywords = ['credit', 'card', 'validator','checker','issuer'],   # Keywords that define your package best
  install_requires=[],            # I get to this in a second,
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)