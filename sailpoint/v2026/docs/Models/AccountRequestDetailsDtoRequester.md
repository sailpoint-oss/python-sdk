---
id: v2026-account-request-details-dto-requester
title: AccountRequestDetailsDtoRequester
pagination_label: AccountRequestDetailsDtoRequester
sidebar_label: AccountRequestDetailsDtoRequester
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountRequestDetailsDtoRequester', 'V2026AccountRequestDetailsDtoRequester'] 
slug: /tools/sdk/python/v2026/models/account-request-details-dto-requester
tags: ['SDK', 'Software Development Kit', 'AccountRequestDetailsDtoRequester', 'V2026AccountRequestDetailsDtoRequester']
---

# AccountRequestDetailsDtoRequester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](dto-type) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.v2026.models.account_request_details_dto_requester import AccountRequestDetailsDtoRequester

account_request_details_dto_requester = AccountRequestDetailsDtoRequester(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

