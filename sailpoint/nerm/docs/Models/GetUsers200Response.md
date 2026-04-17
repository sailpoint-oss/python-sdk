---
id: get-users200-response
title: GetUsers200Response
pagination_label: GetUsers200Response
sidebar_label: GetUsers200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetUsers200Response', 'GetUsers200Response'] 
slug: /tools/sdk/python//models/get-users200-response
tags: ['SDK', 'Software Development Kit', 'GetUsers200Response', 'GetUsers200Response']
---

# GetUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**[]User**](user) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_users200_response import GetUsers200Response

get_users200_response = GetUsers200Response(
users=[
                    sailpoint.nerm.models.user.User(
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
                    ],
metadata=sailpoint.nerm.models.metadata.Metadata(
                    limit = 56, 
                    offset = 56, 
                    total = 56, 
                    next = '/endpoint?limit=10&offset=60', 
                    previous = '/endpoint?limit=10&offset=40', )
)

```
[[Back to top]](#) 

