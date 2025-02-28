---
id: document-fields
title: DocumentFields
pagination_label: DocumentFields
sidebar_label: DocumentFields
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DocumentFields', 'DocumentFields'] 
slug: /tools/sdk/python/v3/models/document-fields
tags: ['SDK', 'Software Development Kit', 'DocumentFields', 'DocumentFields']
---

# DocumentFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod** | **str** | Name of the pod. | [optional] 
**org** | **str** | Name of the tenant. | [optional] 
**type** | [**DocumentType**](document-type) |  | [optional] 
**type** | [**DocumentType**](document-type) |  | [optional] 
**version** | **str** | Version number. | [optional] 
}

## Example

```python
from sailpoint.v3.models.document_fields import DocumentFields

document_fields = DocumentFields(
pod='pod01-useast1',
org='org-name',
type='identity',
type='identity',
version='v2'
)

```
[[Back to top]](#) 

