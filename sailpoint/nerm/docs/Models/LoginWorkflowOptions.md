---
id: login-workflow-options
title: LoginWorkflowOptions
pagination_label: LoginWorkflowOptions
sidebar_label: LoginWorkflowOptions
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LoginWorkflowOptions', 'LoginWorkflowOptions'] 
slug: /tools/sdk/python//models/login-workflow-options
tags: ['SDK', 'Software Development Kit', 'LoginWorkflowOptions', 'LoginWorkflowOptions']
---

# LoginWorkflowOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_time** | **int** | Used for login/password reset for when the password will expire. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.login_workflow_options import LoginWorkflowOptions

login_workflow_options = LoginWorkflowOptions(
expiration_time=1
)

```
[[Back to top]](#) 

