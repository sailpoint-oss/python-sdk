---
id: entitlementstatesnapshotjitdetail
title: Entitlementstatesnapshotjitdetail
pagination_label: Entitlementstatesnapshotjitdetail
sidebar_label: Entitlementstatesnapshotjitdetail
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Entitlementstatesnapshotjitdetail', 'Entitlementstatesnapshotjitdetail'] 
slug: /tools/sdk/python/access-requests/models/entitlementstatesnapshotjitdetail
tags: ['SDK', 'Software Development Kit', 'Entitlementstatesnapshotjitdetail', 'Entitlementstatesnapshotjitdetail']
---

# Entitlementstatesnapshotjitdetail

A single JIT entitlement snapshot entry from the provisioning plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | Application id for the entitlement attribute (same as EntitlementStateSnapshot.applicationId). | [optional] 
**attribute_name** | **str** | Account attribute name for the entitlement (EntitlementStateSnapshot.attributeName). | [optional] 
**attribute_values** | **[]str** | Entitlement values for that attribute (EntitlementStateSnapshot.attributeValues). | [optional] 
}

## Example

```python
from sailpoint.access_requests.models.entitlementstatesnapshotjitdetail import Entitlementstatesnapshotjitdetail

entitlementstatesnapshotjitdetail = Entitlementstatesnapshotjitdetail(
application_id='2c9180835d2e5168015d32f890ca1581',
attribute_name='groups',
attribute_values=["CN=Engineering,OU=Groups,DC=example,DC=com"]
)

```
[[Back to top]](#) 

