---
id: v2025-role-mining-identity-distribution-distribution-inner
title: RoleMiningIdentityDistributionDistributionInner
pagination_label: RoleMiningIdentityDistributionDistributionInner
sidebar_label: RoleMiningIdentityDistributionDistributionInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RoleMiningIdentityDistributionDistributionInner', 'V2025RoleMiningIdentityDistributionDistributionInner'] 
slug: /tools/sdk/python/v2025/models/role-mining-identity-distribution-distribution-inner
tags: ['SDK', 'Software Development Kit', 'RoleMiningIdentityDistributionDistributionInner', 'V2025RoleMiningIdentityDistributionDistributionInner']
---

# RoleMiningIdentityDistributionDistributionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_value** | **str** | The attribute value that identities are grouped by | [optional] 
**count** | **int** | The number of identities that have this attribute value | [optional] 
}

## Example

```python
from sailpoint.v2025.models.role_mining_identity_distribution_distribution_inner import RoleMiningIdentityDistributionDistributionInner

role_mining_identity_distribution_distribution_inner = RoleMiningIdentityDistributionDistributionInner(
attribute_value='NM Tier 3',
count=6
)

```
[[Back to top]](#) 

