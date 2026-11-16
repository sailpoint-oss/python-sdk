---
id: connector-variant-profile
title: ConnectorVariantProfile
pagination_label: ConnectorVariantProfile
sidebar_label: ConnectorVariantProfile
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ConnectorVariantProfile', 'ConnectorVariantProfile'] 
slug: /tools/sdk/python/machine-account-subtypes/models/connector-variant-profile
tags: ['SDK', 'Software Development Kit', 'ConnectorVariantProfile', 'ConnectorVariantProfile']
---

# ConnectorVariantProfile

Response-only connector-variant profile. Always `null` for `SOURCE` and `CONNECTOR` tiers in this release. Populated when the connector-variant tier is available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the connector variant profile. | [optional] 
**connector_type** | **str** | Connector type of the variant profile, for example `JDBC`. | [optional] [default to '']
**variant** | **str** | Variant name within the connector type, for example `MySql`. | [optional] [default to '']
}

## Example

```python
from sailpoint.machine_account_subtypes.models.connector_variant_profile import ConnectorVariantProfile

connector_variant_profile = ConnectorVariantProfile(
id='65de7634-d315-482c-aad4-7fdbd1e42056',
connector_type='',
variant=''
)

```
[[Back to top]](#) 

