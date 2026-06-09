---
id: identityentitlements
title: Identityentitlements
pagination_label: Identityentitlements
sidebar_label: Identityentitlements
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Identityentitlements', 'Identityentitlements'] 
slug: /tools/sdk/python/v1/models/identityentitlements
tags: ['SDK', 'Software Development Kit', 'Identityentitlements', 'Identityentitlements']
---

# Identityentitlements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ref** | [**Taggedobjectdto**](taggedobjectdto) |  | [optional] 
**tags** | **[]str** | Labels to be applied to object. | [optional] 
}

## Example

```python
from sailpoint.identities_v1.models.identityentitlements import Identityentitlements

identityentitlements = Identityentitlements(
object_ref=sailpoint.identities_v1.models.tagged_object_dto.Tagged Object Dto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
tags=["BU_FINANCE","PCI"]
)

```
[[Back to top]](#) 

