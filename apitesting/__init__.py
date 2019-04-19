"""This module offers the api testing library."""

__version__ = '0.0.1'
import logging

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)8s %(message)s')


from .apitesting import ApiTesting