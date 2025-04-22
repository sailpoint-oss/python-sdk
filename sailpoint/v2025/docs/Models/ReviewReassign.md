---
id: v2025-review-reassign
title: ReviewReassign
pagination_label: ReviewReassign
sidebar_label: ReviewReassign
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ReviewReassign', 'V2025ReviewReassign'] 
slug: /tools/sdk/python/v2025/models/review-reassign
tags: ['SDK', 'Software Development Kit', 'ReviewReassign', 'V2025ReviewReassign']
---

# ReviewReassign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reassign** | [**[]ReassignReference**](reassign-reference) |  | [required]
**reassign_to** | **str** | The ID of the identity to which the certification is reassigned | [required]
**reason** | **str** | The reason comment for why the reassign was made | [required]
}

## Example

```python
from sailpoint.v2025.models.review_reassign import ReviewReassign

review_reassign = ReviewReassign(
reassign=[
                    sailpoint.v2025.models.reassign_reference.ReassignReference(
                        id = 'ef38f94347e94562b5bb8424a56397d8', 
                        type = 'ITEM', )
                    ],
reassign_to='ef38f94347e94562b5bb8424a56397d8',
reason='reassigned for some reason'
)

```
[[Back to top]](#) 

