---
id: objectmappingbulkcreaterequest
title: Objectmappingbulkcreaterequest
pagination_label: Objectmappingbulkcreaterequest
sidebar_label: Objectmappingbulkcreaterequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Objectmappingbulkcreaterequest', 'Objectmappingbulkcreaterequest'] 
slug: /tools/sdk/python/v1/models/objectmappingbulkcreaterequest
tags: ['SDK', 'Software Development Kit', 'Objectmappingbulkcreaterequest', 'Objectmappingbulkcreaterequest']
---

# Objectmappingbulkcreaterequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_objects_mappings** | [**[]Objectmappingrequest**](objectmappingrequest) |  | [required]
}

## Example

```python
from sailpoint.configuration_hub_v1.models.objectmappingbulkcreaterequest import Objectmappingbulkcreaterequest

objectmappingbulkcreaterequest = Objectmappingbulkcreaterequest(
new_objects_mappings=[
                    sailpoint.configuration_hub_v1.models.object_mapping_request.Object Mapping Request(
                        object_type = 'IDENTITY', 
                        json_path = '$.name', 
                        source_value = 'My Governance Group Name', 
                        target_value = 'My New Governance Group Name', 
                        enabled = False, )
                    ]
)

```
[[Back to top]](#) 

