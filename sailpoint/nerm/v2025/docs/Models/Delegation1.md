---
id: delegation1
title: Delegation1
pagination_label: Delegation1
sidebar_label: Delegation1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Delegation1', 'Delegation1'] 
slug: /tools/sdk/python//models/delegation1
tags: ['SDK', 'Software Development Kit', 'Delegation1', 'Delegation1']
---

# Delegation1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the delegation | [optional] 
**delegator_id** | **object** | The id of the delegator user | [optional] 
**delegate_id** | **object** | The id of the delegate user | [optional] 
**expiration** | **datetime** | The expiration date of the delegation | [optional] 
**expired** | **bool** | Indicates if the delegation is expired | [optional] 
**created_at** | **datetime** | The date-time the record created. | [optional] [readonly] 
**updated_at** | **datetime** | The date-time the record was last updated. | [optional] [readonly] 
}

## Example

```python
from sailpoint.nerm.v2025.models.delegation1 import Delegation1

delegation1 = Delegation1(
id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
delegator_id=12345678-1234-5678-1234-123456789012,
delegate_id=87654321-4321-6789-4321-210987654321,
expiration='2023-10-01T12:00Z',
expired=False,
created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
)

```
[[Back to top]](#) 

