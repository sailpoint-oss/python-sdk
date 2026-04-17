---
id: submit-role-request
title: SubmitRoleRequest
pagination_label: SubmitRoleRequest
sidebar_label: SubmitRoleRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitRoleRequest', 'SubmitRoleRequest'] 
slug: /tools/sdk/python//models/submit-role-request
tags: ['SDK', 'Software Development Kit', 'SubmitRoleRequest', 'SubmitRoleRequest']
---

# SubmitRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**Role1**](role1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_role_request import SubmitRoleRequest

submit_role_request = SubmitRoleRequest(
role=sailpoint.nerm.models.role_1.Role_1(
                    uid = 'sponsors_role', 
                    type = 'NeprofileRole', 
                    name = 'Sponsors', 
                    groups = [
                        'ad_group_name'
                        ], )
)

```
[[Back to top]](#) 

