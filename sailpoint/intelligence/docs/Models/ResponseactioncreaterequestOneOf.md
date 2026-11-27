---
id: responseactioncreaterequest-one-of
title: ResponseactioncreaterequestOneOf
pagination_label: ResponseactioncreaterequestOneOf
sidebar_label: ResponseactioncreaterequestOneOf
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ResponseactioncreaterequestOneOf', 'ResponseactioncreaterequestOneOf'] 
slug: /tools/sdk/python/intelligence/models/responseactioncreaterequest-one-of
tags: ['SDK', 'Software Development Kit', 'ResponseactioncreaterequestOneOf', 'ResponseactioncreaterequestOneOf']
---

# ResponseactioncreaterequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** |  **Enum** [  'DISABLE_IDENTITY' ] |  | [optional] 
**identity_type** |  **Enum** [  'HUMAN' ] |  | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.responseactioncreaterequest_one_of import ResponseactioncreaterequestOneOf

responseactioncreaterequest_one_of = ResponseactioncreaterequestOneOf(
action_type='DISABLE_IDENTITY',
identity_type='HUMAN'
)

```
[[Back to top]](#) 

