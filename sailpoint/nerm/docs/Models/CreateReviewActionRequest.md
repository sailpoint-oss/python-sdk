---
id: create-review-action-request
title: CreateReviewActionRequest
pagination_label: CreateReviewActionRequest
sidebar_label: CreateReviewActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateReviewActionRequest', 'CreateReviewActionRequest'] 
slug: /tools/sdk/python//models/create-review-action-request
tags: ['SDK', 'Software Development Kit', 'CreateReviewActionRequest', 'CreateReviewActionRequest']
---

# CreateReviewActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**ReviewAction**](review-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_review_action_request import CreateReviewActionRequest

create_review_action_request = CreateReviewActionRequest(
workflow_action=sailpoint.nerm.models.review_action.ReviewAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Allows the requester to review.', 
                    page_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    archived = False, 
                    requires_comment = False, )
)

```
[[Back to top]](#) 

