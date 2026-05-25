---
id: v2026-intel-identity-access-body
title: IntelIdentityAccessBody
pagination_label: IntelIdentityAccessBody
sidebar_label: IntelIdentityAccessBody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelIdentityAccessBody', 'V2026IntelIdentityAccessBody'] 
slug: /tools/sdk/python/v2026/models/intel-identity-access-body
tags: ['SDK', 'Software Development Kit', 'IntelIdentityAccessBody', 'V2026IntelIdentityAccessBody']
---

# IntelIdentityAccessBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**[]IntelAccessAccountWire**](intel-access-account-wire) | Accounts for the identity in camelCase wire format from Shelby List Accounts. | [required]
**privileged_access_items** | [**[]IntelPrivilegedAccessItemWire**](intel-privileged-access-item-wire) | Privileged access items for the identity returned by SDS Search. | [required]
}

## Example

```python
from sailpoint.v2026.models.intel_identity_access_body import IntelIdentityAccessBody

intel_identity_access_body = IntelIdentityAccessBody(
accounts=[{id=acc-1, name=pat.example, source={id=src-1, name=Active Directory}, disabled=false, locked=false, uncorrelated=false, authoritative=false, systemAccount=false, isMachine=false, hasEntitlements=true, manuallyCorrelated=false, connectionType=direct, nativeIdentity=CN=pat,OU=users, created=2026-01-01T00:00:00Z, modified=2026-05-01T00:00:00Z}],
privileged_access_items=[{privileged=true, displayName=Absence_Administrator, name=Absence_Administrator, standalone=true, id=ent-1, source={name=Workday, id=src-2}, attribute=USER_BASED_SECURITY_GROUPS, type=ENTITLEMENT, value=Absence_Administrator}]
)

```
[[Back to top]](#) 

