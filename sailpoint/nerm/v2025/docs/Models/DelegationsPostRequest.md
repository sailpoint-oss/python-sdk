---
id: delegations-post-request
title: DelegationsPostRequest
pagination_label: DelegationsPostRequest
sidebar_label: DelegationsPostRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DelegationsPostRequest', 'DelegationsPostRequest'] 
slug: /tools/sdk/python//models/delegations-post-request
tags: ['SDK', 'Software Development Kit', 'DelegationsPostRequest', 'DelegationsPostRequest']
---

# DelegationsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegation** | [**Delegation2**](delegation2) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.v2025.models.delegations_post_request import DelegationsPostRequest

delegations_post_request = DelegationsPostRequest(
delegation=sailpoint.nerm.v2025.models.delegation_2.Delegation_2(
                    delegator_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    delegate_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    expiration = '2023-10-01T12:00Z', )
)

```
[[Back to top]](#) 

