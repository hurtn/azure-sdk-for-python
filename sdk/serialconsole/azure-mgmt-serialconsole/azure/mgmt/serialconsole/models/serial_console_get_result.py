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

from msrest.serialization import Model


class SerialConsoleGetResult(Model):
    """Serial Console GET Result.

    Returns whether or not Serial Console is disabled.

    :param value: Whether or not Serial Console is disabled.
    :type value: bool
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(SerialConsoleGetResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
