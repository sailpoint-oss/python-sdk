---
id: violationreassigninput
title: Violationreassigninput
pagination_label: Violationreassigninput
sidebar_label: Violationreassigninput
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Violationreassigninput', 'Violationreassigninput'] 
slug: /tools/sdk/python/sod-violations/models/violationreassigninput
tags: ['SDK', 'Software Development Kit', 'Violationreassigninput', 'Violationreassigninput']
---

# Violationreassigninput

Data needed to reassign a policy violation to a new owner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reassign_to** | [**Reassigninput**](reassigninput) |  | [required]
**comments** | **str** | Optional comments explaining the reassignment. | [optional] 
}

## Example

```python
from sailpoint.sod_violations.models.violationreassigninput import Violationreassigninput

violationreassigninput = Violationreassigninput(
reassign_to=sailpoint.sod_violations.models.reassigninput.Reassigninput(
                    assignee_id = '3e07886555ed43cfb83c85c58d2016e6', 
                    assignee_type = 'IDENTITY', ),
comments='some comments about the reassignment'
)

```
[[Back to top]](#) 

