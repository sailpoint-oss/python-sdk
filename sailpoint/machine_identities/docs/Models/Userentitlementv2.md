---
id: userentitlementv2
title: Userentitlementv2
pagination_label: Userentitlementv2
sidebar_label: Userentitlementv2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Userentitlementv2', 'Userentitlementv2'] 
slug: /tools/sdk/python/machine-identities/models/userentitlementv2
tags: ['SDK', 'Software Development Kit', 'Userentitlementv2', 'Userentitlementv2']
---

# Userentitlementv2

A user entitlement associated to a machine identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | The source ID of the entitlement. | [optional] 
**entitlement_id** | **str** | The ID of the entitlement. | [optional] 
**display_name** | **str** | The display name of the entitlement. | [optional] 
**source** | [**Userentitlementv2Source**](userentitlementv2-source) |  | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.userentitlementv2 import Userentitlementv2

userentitlementv2 = Userentitlementv2(
source_id='5898b7c1-620c-49c6-cccc-cbf81eb4bddd',
entitlement_id='6d28b7c1-620c-49c6-b6d5-cbf81eb4b5fa',
display_name='Entitlement Name',
source=
)

```
[[Back to top]](#) 

