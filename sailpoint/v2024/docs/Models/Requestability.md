---
id: v2024-requestability
title: Requestability
pagination_label: Requestability
sidebar_label: Requestability
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Requestability', 'V2024Requestability'] 
slug: /tools/sdk/python/v2024/models/requestability
tags: ['SDK', 'Software Development Kit', 'Requestability', 'V2024Requestability']
---

# Requestability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments_required** | **bool** | Indicates whether the requester of the containing object must provide comments justifying the request. | [optional] [default to False]
**denial_comments_required** | **bool** | Indicates whether an approver must provide comments when denying the request. | [optional] [default to False]
**reauthorization_required** | **bool** | Indicates whether reauthorization is required for the request. | [optional] [default to False]
**approval_schemes** | [**[]AccessProfileApprovalScheme**](access-profile-approval-scheme) | List describing the steps involved in approving the request. | [optional] 
}

## Example

```python
from sailpoint.v2024.models.requestability import Requestability

requestability = Requestability(
comments_required=True,
denial_comments_required=True,
reauthorization_required=True,
approval_schemes=[
                    sailpoint.v2024.models.access_profile_approval_scheme.AccessProfileApprovalScheme(
                        approver_type = 'GOVERNANCE_GROUP', 
                        approver_id = '46c79819-a69f-49a2-becb-12c971ae66c6', )
                    ]
)

```
[[Back to top]](#) 

