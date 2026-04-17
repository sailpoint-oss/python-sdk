---
id: create-synced-attribute201-response
title: CreateSyncedAttribute201Response
pagination_label: CreateSyncedAttribute201Response
sidebar_label: CreateSyncedAttribute201Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateSyncedAttribute201Response', 'CreateSyncedAttribute201Response'] 
slug: /tools/sdk/python//models/create-synced-attribute201-response
tags: ['SDK', 'Software Development Kit', 'CreateSyncedAttribute201Response', 'CreateSyncedAttribute201Response']
---

# CreateSyncedAttribute201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**synced_attribute** | [**SyncedAttribute**](synced-attribute) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_synced_attribute201_response import CreateSyncedAttribute201Response

create_synced_attribute201_response = CreateSyncedAttribute201Response(
synced_attribute=sailpoint.nerm.models.synced_attribute.SyncedAttribute(
                    id = '1246d8b3-ac29-4015-8154-dea4434a73fa', 
                    profile_type_id = '1246d8b3-ac29-4015-8154-dea4434a73fa', 
                    ne_attribute_id = '1246d8b3-ac29-4015-8154-dea4434a73fa', )
)

```
[[Back to top]](#) 

