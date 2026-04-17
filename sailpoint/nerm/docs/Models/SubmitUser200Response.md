---
id: submit-user200-response
title: SubmitUser200Response
pagination_label: SubmitUser200Response
sidebar_label: SubmitUser200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUser200Response', 'SubmitUser200Response'] 
slug: /tools/sdk/python//models/submit-user200-response
tags: ['SDK', 'Software Development Kit', 'SubmitUser200Response', 'SubmitUser200Response']
---

# SubmitUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](user) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user200_response import SubmitUser200Response

submit_user200_response = SubmitUser200Response(
user=sailpoint.nerm.models.user.User(
                    id = 'db6f8e8b-65c2-47d5-a0db-90bcc4e9df9e', 
                    uid = 'user1', 
                    name = 'myusername', 
                    email = 'test@sailpoint.com', 
                    type = 'NeprofileUser', 
                    title = 'Director', 
                    status = 'Active', 
                    login = 'myLogin', 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    cookies_accepted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    preferred_language = 'fr-CA', 
                    locale = 'fr-CA', 
                    group_strings = 'Admin_group, Developer_group', 
                    sailpoint_identity_id = '9496f8d6ddab49c0bef1e9ee6f1b835a', )
)

```
[[Back to top]](#) 

