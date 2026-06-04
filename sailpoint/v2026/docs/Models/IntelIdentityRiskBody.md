---
id: v2026-intel-identity-risk-body
title: IntelIdentityRiskBody
pagination_label: IntelIdentityRiskBody
sidebar_label: IntelIdentityRiskBody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelIdentityRiskBody', 'V2026IntelIdentityRiskBody'] 
slug: /tools/sdk/python/v2026/models/intel-identity-risk-body
tags: ['SDK', 'Software Development Kit', 'IntelIdentityRiskBody', 'V2026IntelIdentityRiskBody']
---

# IntelIdentityRiskBody

Shared response envelope for risk endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outliers** | [**[]IntelOutlierAccessItem**](intel-outlier-access-item) | Page of outlier access-items associated with the resolved identity outlier. | [required]
**outliers_total** | **int** | Total available outlier access-item count from upstream. | [required]
**links** | [**IntelRiskLinks**](intel-risk-links) | Continuation links map; omitted when no additional page exists. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.intel_identity_risk_body import IntelIdentityRiskBody

intel_identity_risk_body = IntelIdentityRiskBody(
outliers=[{id=outlier-access-001, displayName=Example_Admin_Access, description=null, accessType=ENTITLEMENT, sourceName=Example SaaS Source, extremelyRare=false}],
outliers_total=312,
links=sailpoint.v2026.models.intel_risk_links.IntelRiskLinks(
                    outliers = {href=https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/00000000000000000000000000000000/risk/outliers?limit=250&offset=250}, )
)

```
[[Back to top]](#) 

