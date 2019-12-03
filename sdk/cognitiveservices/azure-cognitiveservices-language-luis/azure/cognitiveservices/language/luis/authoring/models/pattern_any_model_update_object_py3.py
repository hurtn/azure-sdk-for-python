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


class PatternAnyModelUpdateObject(Model):
    """Model object for updating a Pattern.Any entity model.

    :param name: The model name.
    :type name: str
    :param explicit_list: The Pattern.Any explicit list.
    :type explicit_list: list[str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'explicit_list': {'key': 'explicitList', 'type': '[str]'},
    }

    def __init__(self, *, name: str=None, explicit_list=None, **kwargs) -> None:
        super(PatternAnyModelUpdateObject, self).__init__(**kwargs)
        self.name = name
        self.explicit_list = explicit_list