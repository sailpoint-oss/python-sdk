---
id: v2025-machine-identity-updated-owner-changes
title: MachineIdentityUpdatedOwnerChanges
pagination_label: MachineIdentityUpdatedOwnerChanges
sidebar_label: MachineIdentityUpdatedOwnerChanges
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityUpdatedOwnerChanges', 'V2025MachineIdentityUpdatedOwnerChanges'] 
slug: /tools/sdk/python/v2025/models/machine-identity-updated-owner-changes
tags: ['SDK', 'Software Development Kit', 'MachineIdentityUpdatedOwnerChanges', 'V2025MachineIdentityUpdatedOwnerChanges']
---

# MachineIdentityUpdatedOwnerChanges

Changes to owners.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Name of the attribute that changed. | [optional] 
**added** | [**[]MachineIdentityOwnerReference**](machine-identity-owner-reference) | Owners that were added. | [optional] 
**removed** | [**[]MachineIdentityOwnerReference**](machine-identity-owner-reference) | Owners that were removed. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.machine_identity_updated_owner_changes import MachineIdentityUpdatedOwnerChanges

machine_identity_updated_owner_changes = MachineIdentityUpdatedOwnerChanges(
attribute_name='owners',
added=[
                    {type=IDENTITY, id=84d8c1b819144608b8b8bc3b84ddbb7b, name=Jerrie admin3cf084, isPrimary=true}
                    ],
removed=[
                    {type=IDENTITY, id=84d8c1b819144608b8b8bc3b84ddbb7b, name=Jerrie admin3cf084, isPrimary=true}
                    ]
)

```
[[Back to top]](#) 

