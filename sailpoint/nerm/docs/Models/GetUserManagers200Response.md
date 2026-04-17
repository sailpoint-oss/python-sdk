---
id: get-user-managers200-response
title: GetUserManagers200Response
pagination_label: GetUserManagers200Response
sidebar_label: GetUserManagers200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetUserManagers200Response', 'GetUserManagers200Response'] 
slug: /tools/sdk/python//models/get-user-managers200-response
tags: ['SDK', 'Software Development Kit', 'GetUserManagers200Response', 'GetUserManagers200Response']
---

# GetUserManagers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_managers** | [**[]UserManager**](user-manager) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_user_managers200_response import GetUserManagers200Response

get_user_managers200_response = GetUserManagers200Response(
user_managers=[
                    sailpoint.nerm.models.user_manager.UserManager(
                        id = '', 
                        uid = '', 
                        user_id = '', 
                        manager_id = '', )
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

