---
id: lifecycle-comment
title: LifecycleComment
pagination_label: LifecycleComment
sidebar_label: LifecycleComment
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LifecycleComment', 'LifecycleComment'] 
slug: /tools/sdk/python/machine-identities-lifecycle-actions/models/lifecycle-comment
tags: ['SDK', 'Software Development Kit', 'LifecycleComment', 'LifecycleComment']
---

# LifecycleComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_id** | **str** | Server-assigned comment identifier. | [optional] 
**author** | [**LifecycleCommentAuthorReference**](lifecycle-comment-author-reference) |  | [optional] 
**comment** | **str** | Free-text comment body. | [optional] 
**created_at** | **datetime** | Time when the comment was created (ISO-8601). | [optional] 
}

## Example

```python
from sailpoint.machine_identities_lifecycle_actions.models.lifecycle_comment import LifecycleComment

lifecycle_comment = LifecycleComment(
comment_id='cmt-001',
author=sailpoint.machine_identities_lifecycle_actions.models.lifecycle_comment_author_reference.Lifecycle Comment Author Reference(
                    type = 'IDENTITY', 
                    id = '2c9180858082150f0180893dbaf44201', 
                    name = 'Pat Manager', ),
comment='Suspending agent until security review completes',
created_at='2026-05-26T19:00Z'
)

```
[[Back to top]](#) 

