---
id: v2026-workgroup-connection-dto
title: WorkgroupConnectionDto
pagination_label: WorkgroupConnectionDto
sidebar_label: WorkgroupConnectionDto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'WorkgroupConnectionDto', 'V2026WorkgroupConnectionDto'] 
slug: /tools/sdk/python/v2026/models/workgroup-connection-dto
tags: ['SDK', 'Software Development Kit', 'WorkgroupConnectionDto', 'V2026WorkgroupConnectionDto']
---

# WorkgroupConnectionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**WorkgroupConnectionDtoObject**](workgroup-connection-dto-object) |  | [optional] 
**connection_type** |  **Enum** [  'AccessRequestReviewer',    'Owner',    'ManagementWorkgroup' ] | Connection Type. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.workgroup_connection_dto import WorkgroupConnectionDto

workgroup_connection_dto = WorkgroupConnectionDto(
object=,
connection_type='AccessRequestReviewer'
)

```
[[Back to top]](#) 

