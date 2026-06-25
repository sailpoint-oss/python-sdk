---
id: intelidentitynotfoundbody
title: Intelidentitynotfoundbody
pagination_label: Intelidentitynotfoundbody
sidebar_label: Intelidentitynotfoundbody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelidentitynotfoundbody', 'Intelidentitynotfoundbody'] 
slug: /tools/sdk/python/intelligence-package/models/intelidentitynotfoundbody
tags: ['SDK', 'Software Development Kit', 'Intelidentitynotfoundbody', 'Intelidentitynotfoundbody']
---

# Intelidentitynotfoundbody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_code** |  **Enum** [  'IDC_IDENTITY_NOT_FOUND' ] | Constant detail code indicating that no identity matched the supplied filter. | [required]
**message** | **str** | Optional explanatory text describing why no identity was found. | [optional] 
}

## Example

```python
from sailpoint.intelligence_package.models.intelidentitynotfoundbody import Intelidentitynotfoundbody

intelidentitynotfoundbody = Intelidentitynotfoundbody(
detail_code='IDC_IDENTITY_NOT_FOUND',
message='No identity matched the supplied SCIM filter expression.'
)

```
[[Back to top]](#) 

