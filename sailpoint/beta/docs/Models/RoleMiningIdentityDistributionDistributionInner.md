---
id: beta-role-mining-identity-distribution-distribution-inner
title: RoleMiningIdentityDistributionDistributionInner
pagination_label: RoleMiningIdentityDistributionDistributionInner
sidebar_label: RoleMiningIdentityDistributionDistributionInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RoleMiningIdentityDistributionDistributionInner', 'BetaRoleMiningIdentityDistributionDistributionInner'] 
slug: /tools/sdk/python/beta/models/role-mining-identity-distribution-distribution-inner
tags: ['SDK', 'Software Development Kit', 'RoleMiningIdentityDistributionDistributionInner', 'BetaRoleMiningIdentityDistributionDistributionInner']
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
from sailpoint.beta.models.role_mining_identity_distribution_distribution_inner import RoleMiningIdentityDistributionDistributionInner

role_mining_identity_distribution_distribution_inner = RoleMiningIdentityDistributionDistributionInner(
attribute_value='NM Tier 3',
count=6
)

```
[[Back to top]](#) 

