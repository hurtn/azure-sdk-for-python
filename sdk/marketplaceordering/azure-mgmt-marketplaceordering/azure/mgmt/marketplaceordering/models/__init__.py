# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .agreement_terms_py3 import AgreementTerms
    from .error_response_error_py3 import ErrorResponseError
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .resource_py3 import Resource
except (SyntaxError, ImportError):
    from .agreement_terms import AgreementTerms
    from .error_response_error import ErrorResponseError
    from .error_response import ErrorResponse, ErrorResponseException
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .resource import Resource
from .operation_paged import OperationPaged

__all__ = [
    'AgreementTerms',
    'ErrorResponseError',
    'ErrorResponse', 'ErrorResponseException',
    'OperationDisplay',
    'Operation',
    'Resource',
    'OperationPaged',
]
