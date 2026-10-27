---
id: machine-identity-application-counts-ownership
title: MachineIdentityApplicationCountsOwnership
pagination_label: MachineIdentityApplicationCountsOwnership
sidebar_label: MachineIdentityApplicationCountsOwnership
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityApplicationCountsOwnership', 'MachineIdentityApplicationCountsOwnership'] 
slug: /tools/sdk/python/machine-identities/models/machine-identity-application-counts-ownership
tags: ['SDK', 'Software Development Kit', 'MachineIdentityApplicationCountsOwnership', 'MachineIdentityApplicationCountsOwnership']
---

# MachineIdentityApplicationCountsOwnership

Ownership coverage of applications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owned_applications** | **int** | Number of applications that have at least one owner. | [optional] 
**owned_percent** | **int** | Percentage of applications that have at least one owner. | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.machine_identity_application_counts_ownership import MachineIdentityApplicationCountsOwnership

machine_identity_application_counts_ownership = MachineIdentityApplicationCountsOwnership(
owned_applications=95,
owned_percent=79
)

```
[[Back to top]](#) 

