---
id: v2025-account-source-reference
title: AccountSourceReference
pagination_label: AccountSourceReference
sidebar_label: AccountSourceReference
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountSourceReference', 'V2025AccountSourceReference'] 
slug: /tools/sdk/python/v2025/models/account-source-reference
tags: ['SDK', 'Software Development Kit', 'AccountSourceReference', 'V2025AccountSourceReference']
---

# AccountSourceReference

Details about the account source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the source. | [required]
**name** | **str** | The name of the source. | [required]
**alias** | **str** | The alias of the source. | [required]
**owner** | [**AccountSourceReferenceOwner**](account-source-reference-owner) |  | [required]
**governance_group** | [**AccountSourceReferenceGovernanceGroup**](account-source-reference-governance-group) |  | [required]
}

## Example

```python
from sailpoint.v2025.models.account_source_reference import AccountSourceReference

account_source_reference = AccountSourceReference(
id='2c918082814e693601816e09471b29b6',
name='Active Directory',
alias='AD',
owner=sailpoint.v2025.models.account_source_reference_owner.AccountSourceReference_owner(
                    id = 'owner-123', 
                    name = 'owner-name', ),
governance_group=sailpoint.v2025.models.account_source_reference_governance_group.AccountSourceReference_governanceGroup(
                    id = 'group-456', 
                    name = 'governance-group-name', )
)

```
[[Back to top]](#) 

