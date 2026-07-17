---
id: bulk-update-amm-key-value-inner
title: BulkUpdateAMMKeyValueInner
pagination_label: BulkUpdateAMMKeyValueInner
sidebar_label: BulkUpdateAMMKeyValueInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BulkUpdateAMMKeyValueInner', 'BulkUpdateAMMKeyValueInner'] 
slug: /tools/sdk/python/access-model-metadata/models/bulk-update-amm-key-value-inner
tags: ['SDK', 'Software Development Kit', 'BulkUpdateAMMKeyValueInner', 'BulkUpdateAMMKeyValueInner']
---

# BulkUpdateAMMKeyValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | the key of metadata attribute | [required]
**values** | **[]str** | the values of attribute to be updated | [required]
}

## Example

```python
from sailpoint.access_model_metadata.models.bulk_update_amm_key_value_inner import BulkUpdateAMMKeyValueInner

bulk_update_amm_key_value_inner = BulkUpdateAMMKeyValueInner(
attribute='iscFederalClassifications',
values=["secret"]
)

```
[[Back to top]](#) 

