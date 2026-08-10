---
id: appliedcontrolcreate
title: Appliedcontrolcreate
pagination_label: Appliedcontrolcreate
sidebar_label: Appliedcontrolcreate
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Appliedcontrolcreate', 'Appliedcontrolcreate'] 
slug: /tools/sdk/python/sod-violations/models/appliedcontrolcreate
tags: ['SDK', 'Software Development Kit', 'Appliedcontrolcreate', 'Appliedcontrolcreate']
---

# Appliedcontrolcreate

Data needed to apply a compensating control to a policy violation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control** | **str** | The unique identifier of the compensating control to apply. | [required]
**comments** | **str** | Optional comments to capture when applying the control. | [optional] 
}

## Example

```python
from sailpoint.sod_violations.models.appliedcontrolcreate import Appliedcontrolcreate

appliedcontrolcreate = Appliedcontrolcreate(
control='3e07886555ed43cfb83c85c58d2016e6',
comments='Some comments about the applied control'
)

```
[[Back to top]](#) 

