---
id: business-application-additional-owners-inner
title: BusinessApplicationAdditionalOwnersInner
pagination_label: BusinessApplicationAdditionalOwnersInner
sidebar_label: BusinessApplicationAdditionalOwnersInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BusinessApplicationAdditionalOwnersInner', 'BusinessApplicationAdditionalOwnersInner'] 
slug: /tools/sdk/python/business-applications/models/business-application-additional-owners-inner
tags: ['SDK', 'Software Development Kit', 'BusinessApplicationAdditionalOwnersInner', 'BusinessApplicationAdditionalOwnersInner']
---

# BusinessApplicationAdditionalOwnersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.business_applications.models.business_application_additional_owners_inner import BusinessApplicationAdditionalOwnersInner

business_application_additional_owners_inner = BusinessApplicationAdditionalOwnersInner(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

