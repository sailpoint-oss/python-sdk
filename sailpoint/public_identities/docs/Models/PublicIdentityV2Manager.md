---
id: public-identity-v2-manager
title: PublicIdentityV2Manager
pagination_label: PublicIdentityV2Manager
sidebar_label: PublicIdentityV2Manager
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PublicIdentityV2Manager', 'PublicIdentityV2Manager'] 
slug: /tools/sdk/python/public-identities/models/public-identity-v2-manager
tags: ['SDK', 'Software Development Kit', 'PublicIdentityV2Manager', 'PublicIdentityV2Manager']
---

# PublicIdentityV2Manager

Manager reference for a public identity search result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Manager identity id | [required]
**name** | **str** | Manager alias / technical name | [required]
**display_name** | **str** | Manager display name. Null when absent from the search hit. | [required]
}

## Example

```python
from sailpoint.public_identities.models.public_identity_v2_manager import PublicIdentityV2Manager

public_identity_v2_manager = PublicIdentityV2Manager(
id='2c9180a46faadee4016fb4e018c20639',
name='thomas.edison',
display_name='Thomas Edison'
)

```
[[Back to top]](#) 

