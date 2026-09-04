---
id: sod-violation-created-payload-target
title: SODViolationCreatedPayloadTarget
pagination_label: SODViolationCreatedPayloadTarget
sidebar_label: SODViolationCreatedPayloadTarget
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SODViolationCreatedPayloadTarget', 'SODViolationCreatedPayloadTarget'] 
slug: /tools/sdk/python/triggers/models/sod-violation-created-payload-target
tags: ['SDK', 'Software Development Kit', 'SODViolationCreatedPayloadTarget', 'SODViolationCreatedPayloadTarget']
---

# SODViolationCreatedPayloadTarget

Identity or entity the violation applies to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Target ID. | [optional] 
**type** |  **Enum** [  'IDENTITY' ] | DTO type of the target reference. | [optional] 
}

## Example

```python
from sailpoint.triggers.models.sod_violation_created_payload_target import SODViolationCreatedPayloadTarget

sod_violation_created_payload_target = SODViolationCreatedPayloadTarget(
id='2c9180888380236101838062022f00ea',
type='IDENTITY'
)

```
[[Back to top]](#) 

