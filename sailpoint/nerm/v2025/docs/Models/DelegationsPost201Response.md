---
id: delegations-post201-response
title: DelegationsPost201Response
pagination_label: DelegationsPost201Response
sidebar_label: DelegationsPost201Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DelegationsPost201Response', 'DelegationsPost201Response'] 
slug: /tools/sdk/python//models/delegations-post201-response
tags: ['SDK', 'Software Development Kit', 'DelegationsPost201Response', 'DelegationsPost201Response']
---

# DelegationsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegation** | [**Delegation1**](delegation1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.v2025.models.delegations_post201_response import DelegationsPost201Response

delegations_post201_response = DelegationsPost201Response(
delegation=sailpoint.nerm.v2025.models.delegation_1.Delegation_1(
                    id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    delegator_id = 12345678-1234-5678-1234-123456789012, 
                    delegate_id = 87654321-4321-6789-4321-210987654321, 
                    expiration = '2023-10-01T12:00Z', 
                    expired = False, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
)

```
[[Back to top]](#) 

