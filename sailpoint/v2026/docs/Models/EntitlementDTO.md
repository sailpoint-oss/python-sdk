---
id: v2026-entitlement-dto
title: EntitlementDTO
pagination_label: EntitlementDTO
sidebar_label: EntitlementDTO
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementDTO', 'V2026EntitlementDTO'] 
slug: /tools/sdk/python/v2026/models/entitlement-dto
tags: ['SDK', 'Software Development Kit', 'EntitlementDTO', 'V2026EntitlementDTO']
---

# EntitlementDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | [required]
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**attribute** | **str** | Name of the entitlement attribute | [optional] 
**uuid** | **str** | Unique entitlement identifier within the database | [optional] 
**value** | **str** | Raw value of the entitlement | [optional] 
**description** | **str** | Entitlment description | [optional] 
**source_schema_object_type** | **str** | Schema objectType on the given application that maps to an Account Group | [optional] 
**privileged** | **bool** | Determines if this entitlement is privileged. | [optional] 
**is_group** | **bool** | True when this object is used to represent a group attribute, otherwise it represents an account attribute. For the time being, the property is always true. | [optional] 
**cloud_governed** | **bool** | Determines if this entitlement is governed in the cloud. | [optional] 
**requestable** | **bool** | Determines if this entitlement is requestable. | [optional] 
**cloud_eligible** | **bool** | Determines if this entitlement is cloud eligible. | [optional] 
**attributes** | **object** | Entitlement attributes | [optional] 
**source** | [**EntitlementDTOAllOfSource**](entitlement-dto-all-of-source) |  | [optional] 
**hash** | **str** | Read-only calculated hash value of an entitlement | [optional] 
**direct_permissions** | [**[]PermissionDto**](permission-dto) |  | [optional] 
**inherit_from** | **[]str** | List of parent entitlements | [optional] 
**segments** | **[]str** | List of entitlement segments | [optional] 
**last_refresh** | **str** | Last time the entitlement was refreshed | [optional] 
**idn_service_app** | **str** | IDN service application | [optional] 
**idn_exceptional** | **str** | Informs whether an entitlement is a priviliged one. | [optional] 
**entitlementitlement_aggregated** | **str** | Indicates whether an entitlement was aggregated | [optional] 
**segment_status** | **str** | Segment status (GLOBAL/LOCAL) | [optional] 
**owner** | [**OwnerReferenceDto**](owner-reference-dto) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.entitlement_dto import EntitlementDTO

entitlement_dto = EntitlementDTO(
id='id12345',
name='aName',
created='2015-05-28T14:07:17Z',
modified='2015-05-28T14:07:17Z',
attribute='authorizationType',
uuid='6a099125e1614e4c9024bff6c6159f49',
value='CN=Users,dc=sailpoint,dc=com',
description='some entitlement description',
source_schema_object_type='group',
privileged=True,
is_group=True,
cloud_governed=True,
requestable=True,
cloud_eligible=True,
attributes={cn=Human Resources-bchun2, owner=CN=Fritz.8349b2f31e67,OU=flatfileAD,dc=flatfile,dc=endtoend,dc=com, objectguid=objectguidHuman-Resources-bchun2, description=HR-desc, sysDescriptions={en_US=HR-desc}, entitlementAggregated=true},
source=sailpoint.v2026.models.entitlement_dto_all_of_source.EntitlementDTO_allOf_source(
                    id = '2b86153b97a94abc936c8a11b106aaf8', 
                    value = 'accountant', 
                    type = 'SOURCE', ),
hash='5c8b309fa18a2c76d7fbee2b9e00dba99e4c82de',
direct_permissions=[
                    sailpoint.v2026.models.permission_dto.Permission DTO(
                        rights = HereIsRight1, 
                        target = 'SYS.GV_$TRANSACTION', )
                    ],
inherit_from=[
                    '[a9ced5a52d284b83a7f5595873d35b4e]'
                    ],
segments=[
                    '[students]'
                    ],
last_refresh='2022-06-24T16:12:53.389386Z',
idn_service_app='AppName123',
idn_exceptional='PRIVILEGED',
entitlementitlement_aggregated='true',
segment_status='GLOBAL',
owner=sailpoint.v2026.models.owner_reference_dto.OwnerReferenceDto(
                    id = '2a2fdacca5e345f18bf7970cfbb8fec2', 
                    name = 'identity 1', 
                    type = 'IDENTITY', )
)

```
[[Back to top]](#) 

