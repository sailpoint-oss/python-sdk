---
id: source-owner
title: SourceOwner
pagination_label: SourceOwner
sidebar_label: SourceOwner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceOwner', 'SourceOwner'] 
slug: /tools/sdk/python/v3/models/source-owner
tags: ['SDK', 'Software Development Kit', 'SourceOwner', 'SourceOwner']
---

# SourceOwner

Reference to identity object who owns the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY' ] | Type of object being referenced. | [optional] 
**id** | **str** | Owner identity's ID. | [optional] 
**name** | **str** | Owner identity's human-readable display name. | [optional] 
}

## Example

```python
from sailpoint.v3.models.source_owner import SourceOwner

source_owner = SourceOwner(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='MyName'
)

```
[[Back to top]](#) 

