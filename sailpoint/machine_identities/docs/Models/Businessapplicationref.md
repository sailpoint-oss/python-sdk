---
id: businessapplicationref
title: Businessapplicationref
pagination_label: Businessapplicationref
sidebar_label: Businessapplicationref
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Businessapplicationref', 'Businessapplicationref'] 
slug: /tools/sdk/python/machine-identities/models/businessapplicationref
tags: ['SDK', 'Software Development Kit', 'Businessapplicationref', 'Businessapplicationref']
---

# Businessapplicationref

Reference to a Business Application associated with a machine identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Reference type. | [optional] 
**id** | **str** | Business Application ID. | [optional] 
**name** | **str** | Business Application display name. | [optional] 
**sanctioned_status** | **Sanctionedstatus** |  | [optional] 
**correlation_type** |  **Enum** [  'MANUAL',    'AUTOMATIC' ] | Whether the Business Application reference was manually assigned or automatically correlated. | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.businessapplicationref import Businessapplicationref

businessapplicationref = Businessapplicationref(
type='BUSINESS_APPLICATION',
id='a1b2c3d4-e5f6-7890-abcd-ef1234567890',
name='Cursor',
sanctioned_status='SANCTIONED',
correlation_type='MANUAL'
)

```
[[Back to top]](#) 

