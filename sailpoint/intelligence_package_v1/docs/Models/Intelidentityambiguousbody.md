---
id: intelidentityambiguousbody
title: Intelidentityambiguousbody
pagination_label: Intelidentityambiguousbody
sidebar_label: Intelidentityambiguousbody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelidentityambiguousbody', 'Intelidentityambiguousbody'] 
slug: /tools/sdk/python/v1/models/intelidentityambiguousbody
tags: ['SDK', 'Software Development Kit', 'Intelidentityambiguousbody', 'Intelidentityambiguousbody']
---

# Intelidentityambiguousbody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_code** |  **Enum** [  'IDC_IDENTITY_AMBIGUOUS' ] | Constant detail code indicating that more than one identity matched the filter. | [required]
**message** | **str** | Optional explanatory text describing why the filter was considered ambiguous. | [optional] 
**candidates** | [**[]Intelidentityambiguouscandidate**](intelidentityambiguouscandidate) | Collection of identities that matched the ambiguous filter expression. | [required]
}

## Example

```python
from sailpoint.intelligence_package_v1.models.intelidentityambiguousbody import Intelidentityambiguousbody

intelidentityambiguousbody = Intelidentityambiguousbody(
detail_code='IDC_IDENTITY_AMBIGUOUS',
message='Multiple identities matched the supplied SCIM filter expression.',
candidates=[{"id":"ef38f94347e94562b5bb8424a56397d8","displayName":"Jane Example"},{"id":"ef38f94347e94562b5bb8424a56397d9","displayName":"J. Example"}]
)

```
[[Back to top]](#) 

