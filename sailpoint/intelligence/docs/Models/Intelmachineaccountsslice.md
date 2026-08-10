---
id: intelmachineaccountsslice
title: Intelmachineaccountsslice
pagination_label: Intelmachineaccountsslice
sidebar_label: Intelmachineaccountsslice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelmachineaccountsslice', 'Intelmachineaccountsslice'] 
slug: /tools/sdk/python/intelligence/models/intelmachineaccountsslice
tags: ['SDK', 'Software Development Kit', 'Intelmachineaccountsslice', 'Intelmachineaccountsslice']
---

# Intelmachineaccountsslice

Correlated machine accounts embedded on the non-human identity aggregate. Returns the correlated account set on the wire today (account paging via child routes is not yet released). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[]Intelmachineaccountwire**](intelmachineaccountwire) | Machine account rows correlated to the non-human identity. | [required]
}

## Example

```python
from sailpoint.intelligence.models.intelmachineaccountsslice import Intelmachineaccountsslice

intelmachineaccountsslice = Intelmachineaccountsslice(
items=[
                    sailpoint.intelligence.models.intelmachineaccountwire.Intelmachineaccountwire(
                        id = '2c91808874ff91550175097daaec161c', 
                        name = 'account-name', 
                        native_identity = 'arn:aws:bedrock:us-east-1:336721:agent/ABCDEFGHI', 
                        source = null, 
                        enabled = True, 
                        locked = False, 
                        machine_identity = null, 
                        owner_identity = null, 
                        description = 'Service account for automation', 
                        subtype = 'Service Account', 
                        access_type = 'account', 
                        environment = 'production', 
                        classification_method = 'DISCOVERED', 
                        manually_edited = False, 
                        manually_correlated = False, 
                        has_entitlements = True, 
                        created = '2026-01-01T00:00Z', 
                        modified = '2026-05-01T00:00Z', 
                        attributes = {}, 
                        connector_attributes = {}, )
                    ]
)

```
[[Back to top]](#) 

