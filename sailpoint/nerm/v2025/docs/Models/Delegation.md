---
id: delegation
title: Delegation
pagination_label: Delegation
sidebar_label: Delegation
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Delegation', 'Delegation'] 
slug: /tools/sdk/python//models/delegation
tags: ['SDK', 'Software Development Kit', 'Delegation', 'Delegation']
---

# Delegation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the delegation | [optional] 
**delegator_id** | **object** | The id of the delegator user | [optional] 
**delegate_id** | **object** | The id of the delegate user | [optional] 
**delegator** | [**DelegatorUser**](delegator-user) |  | [optional] 
**delegate** | [**DelegateUser**](delegate-user) |  | [optional] 
**expiration** | **datetime** | The expiration date of the delegation | [optional] 
**expired** | **bool** | Indicates if the delegation is expired | [optional] 
**created_at** | **datetime** | The date-time the record created. | [optional] [readonly] 
**updated_at** | **datetime** | The date-time the record was last updated. | [optional] [readonly] 
}

## Example

```python
from sailpoint.nerm.v2025.models.delegation import Delegation

delegation = Delegation(
id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
delegator_id=12345678-1234-5678-1234-123456789012,
delegate_id=87654321-4321-6789-4321-210987654321,
delegator=sailpoint.nerm.v2025.models.delegator_user.DelegatorUser(
                    id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    uid = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    type = 'NeprofileUser', 
                    name = 'Jane Doe', 
                    email = 'jane@example.com', 
                    status = 'active', 
                    login = 'jane.doe', 
                    last_login = '2024-06-01T12:34:56Z', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
delegate=sailpoint.nerm.v2025.models.delegate_user.DelegateUser(
                    id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    uid = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    type = 'NeprofileUser', 
                    name = 'Jane Doe', 
                    email = 'jane@example.com', 
                    status = 'active', 
                    login = 'jane.doe', 
                    last_login = '2024-06-01T12:34:56Z', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
expiration='2023-10-01T12:00Z',
expired=False,
created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
)

```
[[Back to top]](#) 

