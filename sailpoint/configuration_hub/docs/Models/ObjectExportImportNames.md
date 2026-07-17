---
id: object-export-import-names
title: ObjectExportImportNames
pagination_label: ObjectExportImportNames
sidebar_label: ObjectExportImportNames
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ObjectExportImportNames', 'ObjectExportImportNames'] 
slug: /tools/sdk/python/configuration-hub/models/object-export-import-names
tags: ['SDK', 'Software Development Kit', 'ObjectExportImportNames', 'ObjectExportImportNames']
---

# ObjectExportImportNames


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included_names** | **[]str** | Object names to be included in a backup. | [optional] 
}

## Example

```python
from sailpoint.configuration_hub.models.object_export_import_names import ObjectExportImportNames

object_export_import_names = ObjectExportImportNames(
included_names=[
                    'Test Object name'
                    ]
)

```
[[Back to top]](#) 

