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

from msrest.paging import Paged


class BlueprintPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Blueprint <azure.mgmt.blueprint.models.Blueprint>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Blueprint]'}
    }

    def __init__(self, *args, **kwargs):

        super(BlueprintPaged, self).__init__(*args, **kwargs)
