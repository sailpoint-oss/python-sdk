---
id: userentitlementv2-source
title: Userentitlementv2Source
pagination_label: Userentitlementv2Source
sidebar_label: Userentitlementv2Source
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Userentitlementv2Source', 'Userentitlementv2Source'] 
slug: /tools/sdk/python/machine-identities/models/userentitlementv2-source
tags: ['SDK', 'Software Development Kit', 'Userentitlementv2Source', 'Userentitlementv2Source']
---

# Userentitlementv2Source

The source of the entitlement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **Dtotype** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.userentitlementv2_source import Userentitlementv2Source

userentitlementv2_source = Userentitlementv2Source(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

