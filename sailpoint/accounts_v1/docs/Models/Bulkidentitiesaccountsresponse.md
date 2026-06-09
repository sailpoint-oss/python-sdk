---
id: bulkidentitiesaccountsresponse
title: Bulkidentitiesaccountsresponse
pagination_label: Bulkidentitiesaccountsresponse
sidebar_label: Bulkidentitiesaccountsresponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Bulkidentitiesaccountsresponse', 'Bulkidentitiesaccountsresponse'] 
slug: /tools/sdk/python/v1/models/bulkidentitiesaccountsresponse
tags: ['SDK', 'Software Development Kit', 'Bulkidentitiesaccountsresponse', 'Bulkidentitiesaccountsresponse']
---

# Bulkidentitiesaccountsresponse

Bulk response object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of bulk request item. | [optional] 
**status_code** | **int** | Response status value. | [optional] 
**message** | **str** | Status containing additional context information about failures. | [optional] 
}

## Example

```python
from sailpoint.accounts_v1.models.bulkidentitiesaccountsresponse import Bulkidentitiesaccountsresponse

bulkidentitiesaccountsresponse = Bulkidentitiesaccountsresponse(
id='2c9180858082150f0180893dbaf553fe',
status_code=404,
message='Referenced identity "2c9180858082150f0180893dbaf553fe" was not found.'
)

```
[[Back to top]](#) 

