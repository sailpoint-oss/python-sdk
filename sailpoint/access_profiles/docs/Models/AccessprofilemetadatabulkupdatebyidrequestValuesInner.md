---
id: accessprofilemetadatabulkupdatebyidrequest-values-inner
title: AccessprofilemetadatabulkupdatebyidrequestValuesInner
pagination_label: AccessprofilemetadatabulkupdatebyidrequestValuesInner
sidebar_label: AccessprofilemetadatabulkupdatebyidrequestValuesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessprofilemetadatabulkupdatebyidrequestValuesInner', 'AccessprofilemetadatabulkupdatebyidrequestValuesInner'] 
slug: /tools/sdk/python/access-profiles/models/accessprofilemetadatabulkupdatebyidrequest-values-inner
tags: ['SDK', 'Software Development Kit', 'AccessprofilemetadatabulkupdatebyidrequestValuesInner', 'AccessprofilemetadatabulkupdatebyidrequestValuesInner']
---

# AccessprofilemetadatabulkupdatebyidrequestValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The technical name of the metadata attribute. | [required]
**values** | **[]str** | The values of the attribute to be updated. | [required]
**object_type** | **str** | The type of the metadata attribute. Set to `custom` for custom metadata attributes, which require a suite license. | [optional] 
}

## Example

```python
from sailpoint.access_profiles.models.accessprofilemetadatabulkupdatebyidrequest_values_inner import AccessprofilemetadatabulkupdatebyidrequestValuesInner

accessprofilemetadatabulkupdatebyidrequest_values_inner = AccessprofilemetadatabulkupdatebyidrequestValuesInner(
attribute='iscFederalClassifications',
values=["secret"],
object_type='custom'
)

```
[[Back to top]](#) 

