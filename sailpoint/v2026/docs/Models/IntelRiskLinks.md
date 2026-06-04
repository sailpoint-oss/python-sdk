---
id: v2026-intel-risk-links
title: IntelRiskLinks
pagination_label: IntelRiskLinks
sidebar_label: IntelRiskLinks
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelRiskLinks', 'V2026IntelRiskLinks'] 
slug: /tools/sdk/python/v2026/models/intel-risk-links
tags: ['SDK', 'Software Development Kit', 'IntelRiskLinks', 'V2026IntelRiskLinks']
---

# IntelRiskLinks

Continuation links for risk responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outliers** | [**IntelHref**](intel-href) | Link to fetch the next outlier page for the same identity. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.intel_risk_links import IntelRiskLinks

intel_risk_links = IntelRiskLinks(
outliers=sailpoint.v2026.models.intel_href.IntelHref(
                    href = '/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access', )
)

```
[[Back to top]](#) 

