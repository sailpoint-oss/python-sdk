---
id: v2026-intel-identity-ambiguous-candidate
title: IntelIdentityAmbiguousCandidate
pagination_label: IntelIdentityAmbiguousCandidate
sidebar_label: IntelIdentityAmbiguousCandidate
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelIdentityAmbiguousCandidate', 'V2026IntelIdentityAmbiguousCandidate'] 
slug: /tools/sdk/python/v2026/models/intel-identity-ambiguous-candidate
tags: ['SDK', 'Software Development Kit', 'IntelIdentityAmbiguousCandidate', 'V2026IntelIdentityAmbiguousCandidate']
---

# IntelIdentityAmbiguousCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identity identifier for one of the ambiguous matching identities. | [required]
**display_name** | **str** | Display name for the ambiguous matching identity when available. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.intel_identity_ambiguous_candidate import IntelIdentityAmbiguousCandidate

intel_identity_ambiguous_candidate = IntelIdentityAmbiguousCandidate(
id='ef38f94347e94562b5bb8424a56397d8',
display_name='Jane Example'
)

```
[[Back to top]](#) 

