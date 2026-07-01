---
id: provisioningpolicydtov1
title: Provisioningpolicydtov1
pagination_label: Provisioningpolicydtov1
sidebar_label: Provisioningpolicydtov1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Provisioningpolicydtov1', 'Provisioningpolicydtov1'] 
slug: /tools/sdk/python/sources/models/provisioningpolicydtov1
tags: ['SDK', 'Software Development Kit', 'Provisioningpolicydtov1', 'Provisioningpolicydtov1']
---

# Provisioningpolicydtov1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the provisioning policy name | [required]
**description** | **str** | the description of the provisioning policy | [optional] 
**usage_type** | **Usagetype** |  | [optional] 
**fields** | [**[]Fielddetailsdtov1**](fielddetailsdtov1) |  | [optional] 
}

## Example

```python
from sailpoint.sources.models.provisioningpolicydtov1 import Provisioningpolicydtov1

provisioningpolicydtov1 = Provisioningpolicydtov1(
name='example provisioning policy for inactive identities',
description='this provisioning policy creates access based on an identity going inactive',
usage_type='CREATE',
fields=[
                    sailpoint.sources.models.field_details_dto.Field Details Dto(
                        name = 'userName', 
                        transform = {"type":"rule","attributes":{"name":"Create Unique LDAP Attribute"}}, 
                        attributes = {"template":"${firstname}.${lastname}${uniqueCounter}","cloudMaxUniqueChecks":"50","cloudMaxSize":"20","cloudRequired":"true"}, 
                        is_required = False, 
                        type = 'string', 
                        is_multi_valued = False, )
                    ]
)

```
[[Back to top]](#) 

