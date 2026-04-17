---
id: submit-users-request
title: SubmitUsersRequest
pagination_label: SubmitUsersRequest
sidebar_label: SubmitUsersRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUsersRequest', 'SubmitUsersRequest'] 
slug: /tools/sdk/python//models/submit-users-request
tags: ['SDK', 'Software Development Kit', 'SubmitUsersRequest', 'SubmitUsersRequest']
---

# SubmitUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**[]User1**](user1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_users_request import SubmitUsersRequest

submit_users_request = SubmitUsersRequest(
users=[
                    sailpoint.nerm.models.user_1.User_1(
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
                    ]
)

```
[[Back to top]](#) 

