---
id: createdatadictionaryfieldrequest
title: Createdatadictionaryfieldrequest
pagination_label: Createdatadictionaryfieldrequest
sidebar_label: Createdatadictionaryfieldrequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Createdatadictionaryfieldrequest', 'Createdatadictionaryfieldrequest'] 
slug: /tools/sdk/python/data-access-security/models/createdatadictionaryfieldrequest
tags: ['SDK', 'Software Development Kit', 'Createdatadictionaryfieldrequest', 'Createdatadictionaryfieldrequest']
---

# Createdatadictionaryfieldrequest

Request body for creating a custom data dictionary field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique field name to create. | [required]
**data_dictionary_type** |  **Enum** [  'Users',    'Roles',    'Permission Types',    'Business Resources' ] | The data dictionary that owns this field. | [required]
}

## Example

```python
from sailpoint.data_access_security.models.createdatadictionaryfieldrequest import Createdatadictionaryfieldrequest

createdatadictionaryfieldrequest = Createdatadictionaryfieldrequest(
name='Department',
data_dictionary_type='Users'
)

```
[[Back to top]](#) 

