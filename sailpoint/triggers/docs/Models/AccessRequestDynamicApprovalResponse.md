---
id: access-request-dynamic-approval-response
title: AccessRequestDynamicApprovalResponse
pagination_label: AccessRequestDynamicApprovalResponse
sidebar_label: AccessRequestDynamicApprovalResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessRequestDynamicApprovalResponse', 'AccessRequestDynamicApprovalResponse'] 
slug: /tools/sdk/python/triggers/models/access-request-dynamic-approval-response
tags: ['SDK', 'Software Development Kit', 'AccessRequestDynamicApprovalResponse', 'AccessRequestDynamicApprovalResponse']
---

# AccessRequestDynamicApprovalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the approver to add to the approval process. If there is none, send an empty value \"\". | [required]
**type** |  **Enum** [  'IDENTITY',    'GOVERNANCE_GROUP' ] | Type of approver to add to the approval process. If there is none, send an empty value \"\". | [required]
**name** | **str** | Name of the approver to add to the approval process. If there is none, send an empty value \"\". | [required]
}

## Example

```python
from sailpoint.triggers.models.access_request_dynamic_approval_response import AccessRequestDynamicApprovalResponse

access_request_dynamic_approval_response = AccessRequestDynamicApprovalResponse(
id='2c91808b6ef1d43e016efba0ce470906',
type='IDENTITY',
name='Adam Adams'
)

```
[[Back to top]](#) 

