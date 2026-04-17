---
id: delegations-get200-response
title: DelegationsGet200Response
pagination_label: DelegationsGet200Response
sidebar_label: DelegationsGet200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DelegationsGet200Response', 'DelegationsGet200Response'] 
slug: /tools/sdk/python//models/delegations-get200-response
tags: ['SDK', 'Software Development Kit', 'DelegationsGet200Response', 'DelegationsGet200Response']
---

# DelegationsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegations** | [**[]Delegation**](delegation) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.delegations_get200_response import DelegationsGet200Response

delegations_get200_response = DelegationsGet200Response(
delegations=[
                    sailpoint.nerm.models.delegation.Delegation(
                        id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                        delegator_id = 12345678-1234-5678-1234-123456789012, 
                        delegate_id = 87654321-4321-6789-4321-210987654321, 
                        expiration = '2023-10-01T12:00Z', 
                        expired = False, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
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

