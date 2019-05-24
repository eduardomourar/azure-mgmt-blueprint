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


class SecretValueReference(Model):
    """Reference to a Key Vault secret.

    All required parameters must be populated in order to send to Azure.

    :param key_vault: Required. Specifies the reference to a given Azure Key
     Vault.
    :type key_vault: ~azure.mgmt.blueprint.models.KeyVaultReference
    :param secret_name: Required. Name of the secret.
    :type secret_name: str
    :param secret_version: The version of the secret to use. If left blank,
     the latest version of the secret is used.
    :type secret_version: str
    """

    _validation = {
        'key_vault': {'required': True},
        'secret_name': {'required': True},
    }

    _attribute_map = {
        'key_vault': {'key': 'keyVault', 'type': 'KeyVaultReference'},
        'secret_name': {'key': 'secretName', 'type': 'str'},
        'secret_version': {'key': 'secretVersion', 'type': 'str'},
    }

    def __init__(self, *, key_vault, secret_name: str, secret_version: str=None, **kwargs) -> None:
        super(SecretValueReference, self).__init__(**kwargs)
        self.key_vault = key_vault
        self.secret_name = secret_name
        self.secret_version = secret_version
