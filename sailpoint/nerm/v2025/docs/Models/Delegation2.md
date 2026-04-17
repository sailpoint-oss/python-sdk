---
id: delegation2
title: Delegation2
pagination_label: Delegation2
sidebar_label: Delegation2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Delegation2', 'Delegation2'] 
slug: /tools/sdk/python//models/delegation2
tags: ['SDK', 'Software Development Kit', 'Delegation2', 'Delegation2']
---

# Delegation2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegator_id** | **str** | The id of the delegator | [optional] 
**delegate_id** | **str** | The id of the delegate | [optional] 
**expiration** | **datetime** | The expiration date of the delegation | [optional] 
}

## Example

```python
from sailpoint.nerm.v2025.models.delegation2 import Delegation2

delegation2 = Delegation2(
delegator_id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
delegate_id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
expiration='2023-10-01T12:00Z'
)

```
[[Back to top]](#) 

