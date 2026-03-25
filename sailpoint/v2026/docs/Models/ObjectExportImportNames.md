---
id: v2026-object-export-import-names
title: ObjectExportImportNames
pagination_label: ObjectExportImportNames
sidebar_label: ObjectExportImportNames
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ObjectExportImportNames', 'V2026ObjectExportImportNames'] 
slug: /tools/sdk/python/v2026/models/object-export-import-names
tags: ['SDK', 'Software Development Kit', 'ObjectExportImportNames', 'V2026ObjectExportImportNames']
---

# ObjectExportImportNames


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included_names** | **[]str** | Object names to be included in a backup. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.object_export_import_names import ObjectExportImportNames

object_export_import_names = ObjectExportImportNames(
included_names=[
                    'Test Object name'
                    ]
)

```
[[Back to top]](#) 

