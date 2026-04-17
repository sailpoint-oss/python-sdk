---
id: submit-roles-request
title: SubmitRolesRequest
pagination_label: SubmitRolesRequest
sidebar_label: SubmitRolesRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitRolesRequest', 'SubmitRolesRequest'] 
slug: /tools/sdk/python//models/submit-roles-request
tags: ['SDK', 'Software Development Kit', 'SubmitRolesRequest', 'SubmitRolesRequest']
---

# SubmitRolesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**[]Role1**](role1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_roles_request import SubmitRolesRequest

submit_roles_request = SubmitRolesRequest(
roles=[
                    sailpoint.nerm.models.role_1.Role_1(
                        uid = 'sponsors_role', 
                        type = 'NeprofileRole', 
                        name = 'Sponsors', 
                        groups = [
                            'ad_group_name'
                            ], )
                    ]
)

```
[[Back to top]](#) 

