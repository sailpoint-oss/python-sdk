---
id: submit-user-role200-response
title: SubmitUserRole200Response
pagination_label: SubmitUserRole200Response
sidebar_label: SubmitUserRole200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserRole200Response', 'SubmitUserRole200Response'] 
slug: /tools/sdk/python//models/submit-user-role200-response
tags: ['SDK', 'Software Development Kit', 'SubmitUserRole200Response', 'SubmitUserRole200Response']
---

# SubmitUserRole200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_role** | [**UserRole**](user-role) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_role200_response import SubmitUserRole200Response

submit_user_role200_response = SubmitUserRole200Response(
user_role=sailpoint.nerm.models.user_role.UserRole(
                    id = '', 
                    uid = '', 
                    user_id = '', 
                    role_id = '', )
)

```
[[Back to top]](#) 

