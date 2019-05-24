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

from .blueprint_resource_status_base import BlueprintResourceStatusBase


class AssignmentStatus(BlueprintResourceStatusBase):
    """The status of a blueprint assignment. This field is readonly.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar time_created: Creation time of this blueprint definition.
    :vartype time_created: datetime
    :ivar last_modified: Last modified time of this blueprint definition.
    :vartype last_modified: datetime
    """

    _validation = {
        'time_created': {'readonly': True},
        'last_modified': {'readonly': True},
    }

    _attribute_map = {
        'time_created': {'key': 'timeCreated', 'type': 'iso-8601'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(AssignmentStatus, self).__init__(**kwargs)
