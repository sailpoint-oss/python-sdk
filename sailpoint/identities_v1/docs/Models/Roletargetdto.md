---
id: roletargetdto
title: Roletargetdto
pagination_label: Roletargetdto
sidebar_label: Roletargetdto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Roletargetdto', 'Roletargetdto'] 
slug: /tools/sdk/python/v1/models/roletargetdto
tags: ['SDK', 'Software Development Kit', 'Roletargetdto', 'Roletargetdto']
---

# Roletargetdto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**Basereferencedto**](basereferencedto) |  | [optional] 
**account_info** | [**Accountinfodto**](accountinfodto) |  | [optional] 
**role** | [**Basereferencedto**](basereferencedto) |  | [optional] 
}

## Example

```python
from sailpoint.identities_v1.models.roletargetdto import Roletargetdto

roletargetdto = Roletargetdto(
source=sailpoint.identities_v1.models.base_reference_dto.Base Reference Dto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
account_info=sailpoint.identities_v1.models.account_info_dto.Account Info Dto(
                    native_identity = 'CN=Abby Smith,OU=Austin,OU=Americas,OU=Demo,DC=seri,DC=acme,DC=com', 
                    display_name = 'Abby.Smith', 
                    uuid = '{ad9fc391-246d-40af-b248-b6556a2b7c01}', ),
role=sailpoint.identities_v1.models.base_reference_dto.Base Reference Dto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', )
)

```
[[Back to top]](#) 

