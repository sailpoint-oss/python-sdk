---
id: beta-workgroup-connection-dto
title: WorkgroupConnectionDto
pagination_label: WorkgroupConnectionDto
sidebar_label: WorkgroupConnectionDto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'WorkgroupConnectionDto', 'BetaWorkgroupConnectionDto'] 
slug: /tools/sdk/python/beta/models/workgroup-connection-dto
tags: ['SDK', 'Software Development Kit', 'WorkgroupConnectionDto', 'BetaWorkgroupConnectionDto']
---

# WorkgroupConnectionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**ConnectedObject**](connected-object) |  | [optional] 
**connection_type** |  **Enum** [  'AccessRequestReviewer',    'Owner',    'ManagementWorkgroup' ] | Connection Type. | [optional] 
}

## Example

```python
from sailpoint.beta.models.workgroup_connection_dto import WorkgroupConnectionDto

workgroup_connection_dto = WorkgroupConnectionDto(
object=sailpoint.beta.models.connected_object.ConnectedObject(
                    type = 'ACCESS_PROFILE', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'Employee-database-read-write', 
                    description = 'Collection of entitlements to read/write the employee database.', ),
connection_type='AccessRequestReviewer'
)

```
[[Back to top]](#) 

