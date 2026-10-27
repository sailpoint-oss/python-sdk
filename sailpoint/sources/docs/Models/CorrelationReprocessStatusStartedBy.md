---
id: correlation-reprocess-status-started-by
title: CorrelationReprocessStatusStartedBy
pagination_label: CorrelationReprocessStatusStartedBy
sidebar_label: CorrelationReprocessStatusStartedBy
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CorrelationReprocessStatusStartedBy', 'CorrelationReprocessStatusStartedBy'] 
slug: /tools/sdk/python/sources/models/correlation-reprocess-status-started-by
tags: ['SDK', 'Software Development Kit', 'CorrelationReprocessStatusStartedBy', 'CorrelationReprocessStatusStartedBy']
---

# CorrelationReprocessStatusStartedBy

Identity that started the run. `null` when the run was not started by an identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.sources.models.correlation_reprocess_status_started_by import CorrelationReprocessStatusStartedBy

correlation_reprocess_status_started_by = CorrelationReprocessStatusStartedBy(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

