---
id: reassigninput
title: Reassigninput
pagination_label: Reassigninput
sidebar_label: Reassigninput
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Reassigninput', 'Reassigninput'] 
slug: /tools/sdk/python/sod-violations/models/reassigninput
tags: ['SDK', 'Software Development Kit', 'Reassigninput', 'Reassigninput']
---

# Reassigninput

The identity or governance group to which a policy violation is reassigned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee_id** | **str** | The unique identifier of the identity or governance group receiving the violation. | [required]
**assignee_type** |  **Enum** [  'IDENTITY',    'GOVERNANCE_GROUP' ] | The type of assignee receiving the violation. | [required]
}

## Example

```python
from sailpoint.sod_violations.models.reassigninput import Reassigninput

reassigninput = Reassigninput(
assignee_id='3e07886555ed43cfb83c85c58d2016e6',
assignee_type='IDENTITY'
)

```
[[Back to top]](#) 

