---
id: lifecycle-action-submit-comment
title: LifecycleActionSubmitComment
pagination_label: LifecycleActionSubmitComment
sidebar_label: LifecycleActionSubmitComment
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LifecycleActionSubmitComment', 'LifecycleActionSubmitComment'] 
slug: /tools/sdk/python/machine-identities-lifecycle-actions/models/lifecycle-action-submit-comment
tags: ['SDK', 'Software Development Kit', 'LifecycleActionSubmitComment', 'LifecycleActionSubmitComment']
---

# LifecycleActionSubmitComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Free-text comment submitted with the lifecycle action request. | [required]
}

## Example

```python
from sailpoint.machine_identities_lifecycle_actions.models.lifecycle_action_submit_comment import LifecycleActionSubmitComment

lifecycle_action_submit_comment = LifecycleActionSubmitComment(
comment='Suspending agent until security review completes'
)

```
[[Back to top]](#) 

