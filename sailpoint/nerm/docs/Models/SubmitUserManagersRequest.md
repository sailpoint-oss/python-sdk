---
id: submit-user-managers-request
title: SubmitUserManagersRequest
pagination_label: SubmitUserManagersRequest
sidebar_label: SubmitUserManagersRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserManagersRequest', 'SubmitUserManagersRequest'] 
slug: /tools/sdk/python//models/submit-user-managers-request
tags: ['SDK', 'Software Development Kit', 'SubmitUserManagersRequest', 'SubmitUserManagersRequest']
---

# SubmitUserManagersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_managers** | [**[]UserManager1**](user-manager1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_managers_request import SubmitUserManagersRequest

submit_user_managers_request = SubmitUserManagersRequest(
user_managers=[
                    sailpoint.nerm.models.user_manager_1.UserManager_1(
                        user_id = '', 
                        manager_id = '', )
                    ]
)

```
[[Back to top]](#) 

