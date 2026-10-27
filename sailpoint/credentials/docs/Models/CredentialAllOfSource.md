---
id: credential-all-of-source
title: CredentialAllOfSource
pagination_label: CredentialAllOfSource
sidebar_label: CredentialAllOfSource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CredentialAllOfSource', 'CredentialAllOfSource'] 
slug: /tools/sdk/python/credentials/models/credential-all-of-source
tags: ['SDK', 'Software Development Kit', 'CredentialAllOfSource', 'CredentialAllOfSource']
---

# CredentialAllOfSource

The source the credential was discovered from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.credentials.models.credential_all_of_source import CredentialAllOfSource

credential_all_of_source = CredentialAllOfSource(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

