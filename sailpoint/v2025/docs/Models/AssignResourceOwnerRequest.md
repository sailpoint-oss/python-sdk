---
id: v2025-assign-resource-owner-request
title: AssignResourceOwnerRequest
pagination_label: AssignResourceOwnerRequest
sidebar_label: AssignResourceOwnerRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AssignResourceOwnerRequest', 'V2025AssignResourceOwnerRequest'] 
slug: /tools/sdk/python/v2025/models/assign-resource-owner-request
tags: ['SDK', 'Software Development Kit', 'AssignResourceOwnerRequest', 'V2025AssignResourceOwnerRequest']
---

# AssignResourceOwnerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** | The unique identifier of the application containing the resource. | [optional] 
**full_path** | **str** | The full path to the resource within the application (e.g., file path or object path). | [optional] 
**identity_id** | **str** | The unique identifier (UUID) of the identity to be assigned as the resource owner. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.assign_resource_owner_request import AssignResourceOwnerRequest

assign_resource_owner_request = AssignResourceOwnerRequest(
app_id=12345,
full_path='/shared/hr/documents/employee-records.pdf',
identity_id='d290f1ee-6c54-4b01-90e6-d701748f0851'
)

```
[[Back to top]](#) 

