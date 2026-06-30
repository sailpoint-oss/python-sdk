---
id: intelaccountsslice
title: Intelaccountsslice
pagination_label: Intelaccountsslice
sidebar_label: Intelaccountsslice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelaccountsslice', 'Intelaccountsslice'] 
slug: /tools/sdk/python/intelligence/models/intelaccountsslice
tags: ['SDK', 'Software Development Kit', 'Intelaccountsslice', 'Intelaccountsslice']
---

# Intelaccountsslice

Accounts slice embedded in the aggregate identity response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[]Intelaccessaccountwire**](intelaccessaccountwire) | First page of accounts for the identity. | [required]
**next** | **str** | Absolute URL to the next accounts page; present only when more results exist. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intelaccountsslice import Intelaccountsslice

intelaccountsslice = Intelaccountsslice(
items=[
                    sailpoint.intelligence.models.intelaccessaccountwire.intelaccessaccountwire(
                        id = '2c91808874ff91550175097daaec161c', 
                        name = 'jdoe', 
                        source = sailpoint.intelligence.models.source.source(), 
                        disabled = False, 
                        locked = False, 
                        authoritative = True, 
                        system_account = False, 
                        is_machine = False, 
                        manually_correlated = False, 
                        native_identity = 'CN=jdoe,OU=Users,DC=example,DC=com', 
                        created = '2023-11-01T10:00Z', 
                        modified = '2024-02-15T16:20Z', )
                    ],
next='https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/accounts?limit=10&offset=10'
)

```
[[Back to top]](#) 

