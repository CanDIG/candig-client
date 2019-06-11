"""
Glue for running client code during development

Import this module before using any other module that imports candig.client.
Otherwise, python will look for client in the installed candig package.

See __path__ documentation at:
    https://docs.python.org/2/tutorial/modules.html
"""

import candig
candig.__path__.insert(0, 'candig')
