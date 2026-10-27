---
id: device-all-of-source
title: DeviceAllOfSource
pagination_label: DeviceAllOfSource
sidebar_label: DeviceAllOfSource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DeviceAllOfSource', 'DeviceAllOfSource'] 
slug: /tools/sdk/python/devices/models/device-all-of-source
tags: ['SDK', 'Software Development Kit', 'DeviceAllOfSource', 'DeviceAllOfSource']
---

# DeviceAllOfSource

The source the device was discovered from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.devices.models.device_all_of_source import DeviceAllOfSource

device_all_of_source = DeviceAllOfSource(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

