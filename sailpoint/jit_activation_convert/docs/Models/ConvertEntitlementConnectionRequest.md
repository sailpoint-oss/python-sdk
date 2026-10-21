---
id: convert-entitlement-connection-request
title: ConvertEntitlementConnectionRequest
pagination_label: ConvertEntitlementConnectionRequest
sidebar_label: ConvertEntitlementConnectionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ConvertEntitlementConnectionRequest', 'ConvertEntitlementConnectionRequest'] 
slug: /tools/sdk/python/jit-activation-convert/models/convert-entitlement-connection-request
tags: ['SDK', 'Software Development Kit', 'ConvertEntitlementConnectionRequest', 'ConvertEntitlementConnectionRequest']
---

# ConvertEntitlementConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | The ID of the entitlement connection to convert. | [required]
**target_type** |  **Enum** [  'JIT',    'STANDING' ] | The assignment type to convert the entitlement connection to. | [required]
}

## Example

```python
from sailpoint.jit_activation_convert.models.convert_entitlement_connection_request import ConvertEntitlementConnectionRequest

convert_entitlement_connection_request = ConvertEntitlementConnectionRequest(
connection_id='757fb803-9024-5861-e510-83a56e4c5bd3',
target_type='JIT'
)

```
[[Back to top]](#) 

