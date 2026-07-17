---
id: outlier-value-type
title: OutlierValueType
pagination_label: OutlierValueType
sidebar_label: OutlierValueType
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'OutlierValueType', 'OutlierValueType'] 
slug: /tools/sdk/python/iai-outliers/models/outlier-value-type
tags: ['SDK', 'Software Development Kit', 'OutlierValueType', 'OutlierValueType']
---

# OutlierValueType

The data type of the value field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** |  **Enum** [  'INTEGER',    'FLOAT' ] | The data type of the value field | [optional] 
**ordinal** | **int** | The position of the value type | [optional] 
}

## Example

```python
from sailpoint.iai_outliers.models.outlier_value_type import OutlierValueType

outlier_value_type = OutlierValueType(
name='INTEGER',
ordinal=0
)

```
[[Back to top]](#) 

