---
id: forward-approval-dto
title: ForwardApprovalDto
pagination_label: ForwardApprovalDto
sidebar_label: ForwardApprovalDto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ForwardApprovalDto', 'ForwardApprovalDto'] 
slug: /tools/sdk/python/access-request-approvals/models/forward-approval-dto
tags: ['SDK', 'Software Development Kit', 'ForwardApprovalDto', 'ForwardApprovalDto']
---

# ForwardApprovalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_owner_id** | **str** | The Id of the new owner | [required]
**comment** | **str** | The comment provided by the forwarder | [required]
}

## Example

```python
from sailpoint.access_request_approvals.models.forward_approval_dto import ForwardApprovalDto

forward_approval_dto = ForwardApprovalDto(
new_owner_id='2c91808568c529c60168cca6f90c1314',
comment='2c91808568c529c60168cca6f90c1313'
)

```
[[Back to top]](#) 

