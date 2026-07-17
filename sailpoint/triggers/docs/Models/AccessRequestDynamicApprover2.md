---
id: access-request-dynamic-approver2
title: AccessRequestDynamicApprover2
pagination_label: AccessRequestDynamicApprover2
sidebar_label: AccessRequestDynamicApprover2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessRequestDynamicApprover2', 'AccessRequestDynamicApprover2'] 
slug: /tools/sdk/python/triggers/models/access-request-dynamic-approver2
tags: ['SDK', 'Software Development Kit', 'AccessRequestDynamicApprover2', 'AccessRequestDynamicApprover2']
---

# AccessRequestDynamicApprover2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the identity to add to the approver list for the access request. | [required]
**name** | **str** | The name of the identity to add to the approver list for the access request. | [required]
**type** |  **Enum** [  'IDENTITY',    'GOVERNANCE_GROUP' ] | The type of object being referenced. | [required]
}

## Example

```python
from sailpoint.triggers.models.access_request_dynamic_approver2 import AccessRequestDynamicApprover2

access_request_dynamic_approver2 = AccessRequestDynamicApprover2(
id='2c91808b6ef1d43e016efba0ce470906',
name='Adam Adams',
type='IDENTITY'
)

```
[[Back to top]](#) 

