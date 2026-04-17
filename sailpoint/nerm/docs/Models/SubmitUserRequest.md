---
id: submit-user-request
title: SubmitUserRequest
pagination_label: SubmitUserRequest
sidebar_label: SubmitUserRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserRequest', 'SubmitUserRequest'] 
slug: /tools/sdk/python//models/submit-user-request
tags: ['SDK', 'Software Development Kit', 'SubmitUserRequest', 'SubmitUserRequest']
---

# SubmitUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User1**](user1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_request import SubmitUserRequest

submit_user_request = SubmitUserRequest(
user=sailpoint.nerm.models.user_1.User_1(
                    name = 'Bob', 
                    email = 'test@sailpoint.com', 
                    type = 'NeprofileUser', 
                    profile_id = 'db6f8e8b-65c2-47d5-a0db-90bcc4e9df9e', 
                    title = 'my_user_title', 
                    status = 'Active', 
                    login = 'my_user', 
                    group_strings = 'Administrator_group,Developer_group', 
                    locale = 'fr-CA', 
                    password = 'U*bF7hy9fW', 
                    sailpoint_identity_id = 'db6f8e8b-65c2-47d5-a0db-90bcc4e9df9e', )
)

```
[[Back to top]](#) 

