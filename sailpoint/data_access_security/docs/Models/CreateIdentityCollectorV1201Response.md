---
id: create-identity-collector-v1201-response
title: CreateIdentityCollectorV1201Response
pagination_label: CreateIdentityCollectorV1201Response
sidebar_label: CreateIdentityCollectorV1201Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateIdentityCollectorV1201Response', 'CreateIdentityCollectorV1201Response'] 
slug: /tools/sdk/python/data-access-security/models/create-identity-collector-v1201-response
tags: ['SDK', 'Software Development Kit', 'CreateIdentityCollectorV1201Response', 'CreateIdentityCollectorV1201Response']
---

# CreateIdentityCollectorV1201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the created identity collector. | [optional] 
**name** | **str** | The display name of the created identity collector. | [optional] 
}

## Example

```python
from sailpoint.data_access_security.models.create_identity_collector_v1201_response import CreateIdentityCollectorV1201Response

create_identity_collector_v1201_response = CreateIdentityCollectorV1201Response(
id=12345,
name='Active Directory Identity Collector'
)

```
[[Back to top]](#) 

