---
id: sod-violation-mitigated-payload-applied-controls-inner-applier
title: SODViolationMitigatedPayloadAppliedControlsInnerApplier
pagination_label: SODViolationMitigatedPayloadAppliedControlsInnerApplier
sidebar_label: SODViolationMitigatedPayloadAppliedControlsInnerApplier
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SODViolationMitigatedPayloadAppliedControlsInnerApplier', 'SODViolationMitigatedPayloadAppliedControlsInnerApplier'] 
slug: /tools/sdk/python/triggers/models/sod-violation-mitigated-payload-applied-controls-inner-applier
tags: ['SDK', 'Software Development Kit', 'SODViolationMitigatedPayloadAppliedControlsInnerApplier', 'SODViolationMitigatedPayloadAppliedControlsInnerApplier']
---

# SODViolationMitigatedPayloadAppliedControlsInnerApplier

Identity that applied the control.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Applier ID. | [optional] 
**type** |  **Enum** [  'IDENTITY' ] | DTO type of the applier reference. | [optional] 
}

## Example

```python
from sailpoint.triggers.models.sod_violation_mitigated_payload_applied_controls_inner_applier import SODViolationMitigatedPayloadAppliedControlsInnerApplier

sod_violation_mitigated_payload_applied_controls_inner_applier = SODViolationMitigatedPayloadAppliedControlsInnerApplier(
id='2c918088837fe14901838062029a04bf',
type='IDENTITY'
)

```
[[Back to top]](#) 

