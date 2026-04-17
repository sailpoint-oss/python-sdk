---
id: submit-user-manager200-response
title: SubmitUserManager200Response
pagination_label: SubmitUserManager200Response
sidebar_label: SubmitUserManager200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserManager200Response', 'SubmitUserManager200Response'] 
slug: /tools/sdk/python//models/submit-user-manager200-response
tags: ['SDK', 'Software Development Kit', 'SubmitUserManager200Response', 'SubmitUserManager200Response']
---

# SubmitUserManager200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_manager** | [**UserManager**](user-manager) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_manager200_response import SubmitUserManager200Response

submit_user_manager200_response = SubmitUserManager200Response(
user_manager=sailpoint.nerm.models.user_manager.UserManager(
                    id = '', 
                    uid = '', 
                    user_id = '', 
                    manager_id = '', )
)

```
[[Back to top]](#) 

