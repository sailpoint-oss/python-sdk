---
id: v2026-intel-identity-ambiguous-body
title: IntelIdentityAmbiguousBody
pagination_label: IntelIdentityAmbiguousBody
sidebar_label: IntelIdentityAmbiguousBody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelIdentityAmbiguousBody', 'V2026IntelIdentityAmbiguousBody'] 
slug: /tools/sdk/python/v2026/models/intel-identity-ambiguous-body
tags: ['SDK', 'Software Development Kit', 'IntelIdentityAmbiguousBody', 'V2026IntelIdentityAmbiguousBody']
---

# IntelIdentityAmbiguousBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_code** |  **Enum** [  'IDC_IDENTITY_AMBIGUOUS' ] | Constant detail code indicating that more than one identity matched the filter. | [required]
**message** | **str** | Optional explanatory text describing why the filter was considered ambiguous. | [optional] 
**candidates** | [**[]IntelIdentityAmbiguousCandidate**](intel-identity-ambiguous-candidate) | Collection of identities that matched the ambiguous filter expression. | [required]
}

## Example

```python
from sailpoint.v2026.models.intel_identity_ambiguous_body import IntelIdentityAmbiguousBody

intel_identity_ambiguous_body = IntelIdentityAmbiguousBody(
detail_code='IDC_IDENTITY_AMBIGUOUS',
message='Multiple identities matched the supplied SCIM filter expression.',
candidates=[{id=ef38f94347e94562b5bb8424a56397d8, displayName=Jane Example}, {id=ef38f94347e94562b5bb8424a56397d9, displayName=J. Example}]
)

```
[[Back to top]](#) 

