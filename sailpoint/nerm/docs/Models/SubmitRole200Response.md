---
id: submit-role200-response
title: SubmitRole200Response
pagination_label: SubmitRole200Response
sidebar_label: SubmitRole200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitRole200Response', 'SubmitRole200Response'] 
slug: /tools/sdk/python//models/submit-role200-response
tags: ['SDK', 'Software Development Kit', 'SubmitRole200Response', 'SubmitRole200Response']
---

# SubmitRole200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**Role**](role) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_role200_response import SubmitRole200Response

submit_role200_response = SubmitRole200Response(
role=sailpoint.nerm.models.role.Role(
                    id = '', 
                    uid = 'sponsors_role', 
                    name = 'Sponsors', 
                    groups = [
                        'ad_group_name'
                        ], )
)

```
[[Back to top]](#) 

