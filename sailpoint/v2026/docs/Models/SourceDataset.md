---
id: v2026-source-dataset
title: SourceDataset
pagination_label: SourceDataset
sidebar_label: SourceDataset
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceDataset', 'V2026SourceDataset'] 
slug: /tools/sdk/python/v2026/models/source-dataset
tags: ['SDK', 'Software Development Kit', 'SourceDataset', 'V2026SourceDataset']
---

# SourceDataset

Dataset instance for a source. Fields are read from source-persisted dataset rows in Diana (name/description reflect the source's stored snapshot); aggregationEnabled is stored per source instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Dataset identifier. | [optional] 
**name** | **str** | Display name of the dataset. | [optional] 
**description** | **str** | Description of the dataset. | [optional] 
**aggregation_enabled** | **bool** | Whether aggregation is enabled for this dataset on the source. | [optional] [default to False]
**resources** | [**[]SourceDatasetResourcesInner**](source-dataset-resources-inner) | Simplified resource references associated with this dataset. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.source_dataset import SourceDataset

source_dataset = SourceDataset(
id='cmdb-servicenow:applications',
name='Applications',
description='CMDB application records for this source.',
aggregation_enabled=True,
resources=[
                    sailpoint.v2026.models.source_dataset_resources_inner.SourceDataset_resources_inner(
                        id = 'aws:iam-role', 
                        name = 'Role', )
                    ]
)

```
[[Back to top]](#) 

