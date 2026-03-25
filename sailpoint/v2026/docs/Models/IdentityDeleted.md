---
id: v2026-identity-deleted
title: IdentityDeleted
pagination_label: IdentityDeleted
sidebar_label: IdentityDeleted
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityDeleted', 'V2026IdentityDeleted'] 
slug: /tools/sdk/python/v2026/models/identity-deleted
tags: ['SDK', 'Software Development Kit', 'IdentityDeleted', 'V2026IdentityDeleted']
---

# IdentityDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**IdentityDeletedIdentity**](identity-deleted-identity) |  | [required]
**attributes** | **map[string]object** | The attributes assigned to the identity. Attributes are determined by the identity profile. | [required]
}

## Example

```python
from sailpoint.v2026.models.identity_deleted import IdentityDeleted

identity_deleted = IdentityDeleted(
identity=sailpoint.v2026.models.identity_deleted_identity.IdentityDeleted_identity(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', ),
attributes={firstname=John}
)

```
[[Back to top]](#) 

