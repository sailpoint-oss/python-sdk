---
id: intelidentityaccessbody
title: Intelidentityaccessbody
pagination_label: Intelidentityaccessbody
sidebar_label: Intelidentityaccessbody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelidentityaccessbody', 'Intelidentityaccessbody'] 
slug: /tools/sdk/python/v1/models/intelidentityaccessbody
tags: ['SDK', 'Software Development Kit', 'Intelidentityaccessbody', 'Intelidentityaccessbody']
---

# Intelidentityaccessbody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**[]Intelaccessaccountwire**](intelaccessaccountwire) | Accounts for the identity in camelCase wire format from Shelby List Accounts. | [required]
**privileged_access_items** | [**[]Intelprivilegedaccessitemwire**](intelprivilegedaccessitemwire) | Privileged access items for the identity returned by SDS Search. | [required]
}

## Example

```python
from sailpoint.intelligence_package_v1.models.intelidentityaccessbody import Intelidentityaccessbody

intelidentityaccessbody = Intelidentityaccessbody(
accounts=[{"id":"acc-1","name":"pat.example","source":{"id":"src-1","name":"Active Directory"},"disabled":false,"locked":false,"uncorrelated":false,"authoritative":false,"systemAccount":false,"isMachine":false,"hasEntitlements":true,"manuallyCorrelated":false,"connectionType":"direct","nativeIdentity":"CN=pat,OU=users","created":"2026-01-01T00:00:00Z","modified":"2026-05-01T00:00:00Z"}],
privileged_access_items=[{"privileged":true,"displayName":"Absence_Administrator","name":"Absence_Administrator","standalone":true,"id":"ent-1","source":{"name":"Workday","id":"src-2"},"attribute":"USER_BASED_SECURITY_GROUPS","type":"ENTITLEMENT","value":"Absence_Administrator"}]
)

```
[[Back to top]](#) 

