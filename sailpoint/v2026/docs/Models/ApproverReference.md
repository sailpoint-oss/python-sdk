---
id: v2026-approver-reference
title: ApproverReference
pagination_label: ApproverReference
sidebar_label: ApproverReference
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApproverReference', 'V2026ApproverReference'] 
slug: /tools/sdk/python/v2026/models/approver-reference
tags: ['SDK', 'Software Development Kit', 'ApproverReference', 'V2026ApproverReference']
---

# ApproverReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of supported DtoType like IDENTITY, MACHINE_IDENTITY etc. | [optional] 
**type** | **str** | Type of Dto | [optional] 
**name** | **str** | Display name of DtoType like IDENTITY, MACHINE_IDENTITY etc | [optional] 
}

## Example

```python
from sailpoint.v2026.models.approver_reference import ApproverReference

approver_reference = ApproverReference(
id='85131bd73fdc423599e57f40b29f01fe',
type='IDENTITY',
name='SailPoint Support'
)

```
[[Back to top]](#) 

