---
id: device-os
title: DeviceOS
pagination_label: DeviceOS
sidebar_label: DeviceOS
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DeviceOS', 'DeviceOS'] 
slug: /tools/sdk/python/devices/models/device-os
tags: ['SDK', 'Software Development Kit', 'DeviceOS', 'DeviceOS']
---

# DeviceOS

The operating system reported by the source for a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The operating system type. | [optional] 
**version** | **str** | The operating system version. | [optional] 
}

## Example

```python
from sailpoint.devices.models.device_os import DeviceOS

device_os = DeviceOS(
type='macos',
version='14.5'
)

```
[[Back to top]](#) 

