---
id: submit-user-manager-request
title: SubmitUserManagerRequest
pagination_label: SubmitUserManagerRequest
sidebar_label: SubmitUserManagerRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserManagerRequest', 'SubmitUserManagerRequest'] 
slug: /tools/sdk/python//models/submit-user-manager-request
tags: ['SDK', 'Software Development Kit', 'SubmitUserManagerRequest', 'SubmitUserManagerRequest']
---

# SubmitUserManagerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_manager** | [**UserManager1**](user-manager1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_manager_request import SubmitUserManagerRequest

submit_user_manager_request = SubmitUserManagerRequest(
user_manager=sailpoint.nerm.models.user_manager_1.UserManager_1(
                    user_id = '', 
                    manager_id = '', )
)

```
[[Back to top]](#) 

