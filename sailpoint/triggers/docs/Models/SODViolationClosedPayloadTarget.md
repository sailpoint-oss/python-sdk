---
id: sod-violation-closed-payload-target
title: SODViolationClosedPayloadTarget
pagination_label: SODViolationClosedPayloadTarget
sidebar_label: SODViolationClosedPayloadTarget
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SODViolationClosedPayloadTarget', 'SODViolationClosedPayloadTarget'] 
slug: /tools/sdk/python/triggers/models/sod-violation-closed-payload-target
tags: ['SDK', 'Software Development Kit', 'SODViolationClosedPayloadTarget', 'SODViolationClosedPayloadTarget']
---

# SODViolationClosedPayloadTarget

Identity or entity the violation applied to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Target ID. | [optional] 
**type** |  **Enum** [  'IDENTITY' ] | Target type. | [optional] 
}

## Example

```python
from sailpoint.triggers.models.sod_violation_closed_payload_target import SODViolationClosedPayloadTarget

sod_violation_closed_payload_target = SODViolationClosedPayloadTarget(
id='2c9180888380236101838062022f00ea',
type='IDENTITY'
)

```
[[Back to top]](#) 

