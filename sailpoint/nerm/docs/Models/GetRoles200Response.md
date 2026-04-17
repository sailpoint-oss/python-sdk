---
id: get-roles200-response
title: GetRoles200Response
pagination_label: GetRoles200Response
sidebar_label: GetRoles200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetRoles200Response', 'GetRoles200Response'] 
slug: /tools/sdk/python//models/get-roles200-response
tags: ['SDK', 'Software Development Kit', 'GetRoles200Response', 'GetRoles200Response']
---

# GetRoles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**[]Role**](role) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_roles200_response import GetRoles200Response

get_roles200_response = GetRoles200Response(
roles=[
                    sailpoint.nerm.models.role.Role(
                        id = '', 
                        uid = 'sponsors_role', 
                        name = 'Sponsors', 
                        groups = [
                            'ad_group_name'
                            ], )
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

