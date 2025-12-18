---
id: v2025-application-discovery-response-target
title: ApplicationDiscoveryResponseTarget
pagination_label: ApplicationDiscoveryResponseTarget
sidebar_label: ApplicationDiscoveryResponseTarget
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApplicationDiscoveryResponseTarget', 'V2025ApplicationDiscoveryResponseTarget'] 
slug: /tools/sdk/python/v2025/models/application-discovery-response-target
tags: ['SDK', 'Software Development Kit', 'ApplicationDiscoveryResponseTarget', 'V2025ApplicationDiscoveryResponseTarget']
---

# ApplicationDiscoveryResponseTarget

The target(source) of app discovery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](dto-type) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.v2025.models.application_discovery_response_target import ApplicationDiscoveryResponseTarget

application_discovery_response_target = ApplicationDiscoveryResponseTarget(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

