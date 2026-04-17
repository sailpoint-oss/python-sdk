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
**delegator_id** | **str** | The id of the delegator | [optional] 
**delegate_id** | **str** | The id of the delegate | [optional] 
**expiration** | **datetime** | The expiration date of the delegation | [optional] 
}

## Example

```python
from sailpoint.nerm.models.delegation1 import Delegation1

delegation1 = Delegation1(
delegator_id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
delegate_id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
expiration='2023-10-01T12:00Z'
)

```
[[Back to top]](#) 

