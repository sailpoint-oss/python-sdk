---
id: account-source-reference-governance-group
title: AccountSourceReferenceGovernanceGroup
pagination_label: AccountSourceReferenceGovernanceGroup
sidebar_label: AccountSourceReferenceGovernanceGroup
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountSourceReferenceGovernanceGroup', 'AccountSourceReferenceGovernanceGroup'] 
slug: /tools/sdk/python/triggers/models/account-source-reference-governance-group
tags: ['SDK', 'Software Development Kit', 'AccountSourceReferenceGovernanceGroup', 'AccountSourceReferenceGovernanceGroup']
---

# AccountSourceReferenceGovernanceGroup

Details about the governance group of the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the governance group. | [required]
**name** | **str** | Name of the governance group. | [required]
}

## Example

```python
from sailpoint.triggers.models.account_source_reference_governance_group import AccountSourceReferenceGovernanceGroup

account_source_reference_governance_group = AccountSourceReferenceGovernanceGroup(
id='group-456',
name='governance-group-name'
)

```
[[Back to top]](#) 

