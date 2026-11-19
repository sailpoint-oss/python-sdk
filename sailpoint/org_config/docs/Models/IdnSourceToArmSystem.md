---
id: idn-source-to-arm-system
title: IdnSourceToArmSystem
pagination_label: IdnSourceToArmSystem
sidebar_label: IdnSourceToArmSystem
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdnSourceToArmSystem', 'IdnSourceToArmSystem'] 
slug: /tools/sdk/python/org-config/models/idn-source-to-arm-system
tags: ['SDK', 'Software Development Kit', 'IdnSourceToArmSystem', 'IdnSourceToArmSystem']
---

# IdnSourceToArmSystem

A mapping from an IDN source id to an ARM system id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | The IDN source id. | [optional] 
**system_id** | **str** | The ARM system id. | [optional] 
}

## Example

```python
from sailpoint.org_config.models.idn_source_to_arm_system import IdnSourceToArmSystem

idn_source_to_arm_system = IdnSourceToArmSystem(
source_id='2c91808c791a94e501792388b0d62659',
system_id='1556'
)

```
[[Back to top]](#) 

