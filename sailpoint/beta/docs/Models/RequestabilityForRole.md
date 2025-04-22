---
id: beta-requestability-for-role
title: RequestabilityForRole
pagination_label: RequestabilityForRole
sidebar_label: RequestabilityForRole
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RequestabilityForRole', 'BetaRequestabilityForRole'] 
slug: /tools/sdk/python/beta/models/requestability-for-role
tags: ['SDK', 'Software Development Kit', 'RequestabilityForRole', 'BetaRequestabilityForRole']
---

# RequestabilityForRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments_required** | **bool** | Whether the requester of the containing object must provide comments justifying the request | [optional] [default to False]
**denial_comments_required** | **bool** | Whether an approver must provide comments when denying the request | [optional] [default to False]
**approval_schemes** | [**[]ApprovalSchemeForRole**](approval-scheme-for-role) | List describing the steps in approving the request | [optional] 
}

## Example

```python
from sailpoint.beta.models.requestability_for_role import RequestabilityForRole

requestability_for_role = RequestabilityForRole(
comments_required=True,
denial_comments_required=True,
approval_schemes=[
                    sailpoint.beta.models.approval_scheme_for_role.ApprovalSchemeForRole(
                        approver_type = 'GOVERNANCE_GROUP', 
                        approver_id = '46c79819-a69f-49a2-becb-12c971ae66c6', )
                    ]
)

```
[[Back to top]](#) 

