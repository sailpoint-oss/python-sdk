---
id: capability-owners-primary
title: CapabilityOwnersPrimary
pagination_label: CapabilityOwnersPrimary
sidebar_label: CapabilityOwnersPrimary
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CapabilityOwnersPrimary', 'CapabilityOwnersPrimary'] 
slug: /tools/sdk/python/capabilities/models/capability-owners-primary
tags: ['SDK', 'Software Development Kit', 'CapabilityOwnersPrimary', 'CapabilityOwnersPrimary']
---

# CapabilityOwnersPrimary

The identity selected as the primary owner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.capabilities.models.capability_owners_primary import CapabilityOwnersPrimary

capability_owners_primary = CapabilityOwnersPrimary(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

