---
id: json-patch
title: JsonPatch
pagination_label: JsonPatch
sidebar_label: JsonPatch
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JsonPatch', 'JsonPatch'] 
slug: /tools/sdk/python/configuration-hub/models/json-patch
tags: ['SDK', 'Software Development Kit', 'JsonPatch', 'JsonPatch']
---

# JsonPatch

A JSONPatch document as defined by [RFC 6902 - JSON Patch](https://tools.ietf.org/html/rfc6902)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**[]JsonPatchOperation**](json-patch-operation) | Operations to be applied | [optional] 
}

## Example

```python
from sailpoint.configuration_hub.models.json_patch import JsonPatch

json_patch = JsonPatch(
operations=[
                    sailpoint.configuration_hub.models.json_patch_operation.Json Patch Operation(
                        op = 'replace', 
                        path = '/description', 
                        value = New description, )
                    ]
)

```
[[Back to top]](#) 

