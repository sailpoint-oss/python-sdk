---
id: object-mapping-bulk-create-request
title: ObjectMappingBulkCreateRequest
pagination_label: ObjectMappingBulkCreateRequest
sidebar_label: ObjectMappingBulkCreateRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ObjectMappingBulkCreateRequest', 'ObjectMappingBulkCreateRequest'] 
slug: /tools/sdk/python/configuration-hub/models/object-mapping-bulk-create-request
tags: ['SDK', 'Software Development Kit', 'ObjectMappingBulkCreateRequest', 'ObjectMappingBulkCreateRequest']
---

# ObjectMappingBulkCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_objects_mappings** | [**[]ObjectMappingRequest**](object-mapping-request) |  | [required]
}

## Example

```python
from sailpoint.configuration_hub.models.object_mapping_bulk_create_request import ObjectMappingBulkCreateRequest

object_mapping_bulk_create_request = ObjectMappingBulkCreateRequest(
new_objects_mappings=[
                    sailpoint.configuration_hub.models.object_mapping_request.Object Mapping Request(
                        object_type = 'IDENTITY', 
                        json_path = '$.name', 
                        source_value = 'My Governance Group Name', 
                        target_value = 'My New Governance Group Name', 
                        enabled = False, )
                    ]
)

```
[[Back to top]](#) 

