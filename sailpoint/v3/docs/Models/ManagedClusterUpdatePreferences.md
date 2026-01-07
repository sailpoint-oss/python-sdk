---
id: managed-cluster-update-preferences
title: ManagedClusterUpdatePreferences
pagination_label: ManagedClusterUpdatePreferences
sidebar_label: ManagedClusterUpdatePreferences
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ManagedClusterUpdatePreferences', 'ManagedClusterUpdatePreferences'] 
slug: /tools/sdk/python/v3/models/managed-cluster-update-preferences
tags: ['SDK', 'Software Development Kit', 'ManagedClusterUpdatePreferences', 'ManagedClusterUpdatePreferences']
---

# ManagedClusterUpdatePreferences

The preference for applying updates for the cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_groups** | **str** | The processGroups for updatePreferences | [optional] 
**update_state** |  **Enum** [  'AUTO',    'DISABLED' ] | The current updateState for the cluster | [optional] 
**notification_email** | **str** | The mail id to which new releases will be notified | [optional] 
}

## Example

```python
from sailpoint.v3.models.managed_cluster_update_preferences import ManagedClusterUpdatePreferences

managed_cluster_update_preferences = ManagedClusterUpdatePreferences(
process_groups='processGroup1',
update_state='DISABLED',
notification_email='test@mail.com'
)

```
[[Back to top]](#) 

