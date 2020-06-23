
# -*- coding: utf-8 -*-

r"""NASH Exceptions (API).

Este módulo define todas las excepciones que pueden provocar las APIs de NASH.
"""

# Excepción base.
class NASHError(Exception): pass

# Excepciones derivadas.
class InvalidArgError(NASHError): pass
class NotExistsError(NASHError): pass
class NASHFileSystemError(NASHError): pass