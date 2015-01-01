from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(name='sphinxcontrib-coffee3',
          version='0.0.1',
          license='BSD',
          author="Stephen Sugden, Peter Romianowski",
          author_email="glurgle@gmail.com, honkbert@gmail.com",
          description='Sphinx extension to add CoffeeScript support',
          platforms='any',
          packages=find_packages(),
          namespace_packages=['sphinxcontrib'])
