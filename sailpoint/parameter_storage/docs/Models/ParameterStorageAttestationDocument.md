---
id: parameter-storage-attestation-document
title: ParameterStorageAttestationDocument
pagination_label: ParameterStorageAttestationDocument
sidebar_label: ParameterStorageAttestationDocument
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ParameterStorageAttestationDocument', 'ParameterStorageAttestationDocument'] 
slug: /tools/sdk/python/parameter-storage/models/parameter-storage-attestation-document
tags: ['SDK', 'Software Development Kit', 'ParameterStorageAttestationDocument', 'ParameterStorageAttestationDocument']
---

# ParameterStorageAttestationDocument

The attestation document. This is Base64Url encoded binary data containing the attestation document. This has a cert with a public key that needs to be used to encrypt the private fields of the parameter on creation or update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestation_document** | **str** | The Base64Url encoded attestation document. | [optional] 
}

## Example

```python
from sailpoint.parameter_storage.models.parameter_storage_attestation_document import ParameterStorageAttestationDocument

parameter_storage_attestation_document = ParameterStorageAttestationDocument(
attestation_document='YmFzZTY0IGVuY29kZWQgYXR0ZXN0YXRpb24gZG9jdW1lbnQgZ29lcyBoZXJlLg=='
)

```
[[Back to top]](#) 

