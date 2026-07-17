---
id: account-request-details-dto-requester
title: AccountRequestDetailsDtoRequester
pagination_label: AccountRequestDetailsDtoRequester
sidebar_label: AccountRequestDetailsDtoRequester
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountRequestDetailsDtoRequester', 'AccountRequestDetailsDtoRequester'] 
slug: /tools/sdk/python/machine-account-creation-request/models/account-request-details-dto-requester
tags: ['SDK', 'Software Development Kit', 'AccountRequestDetailsDtoRequester', 'AccountRequestDetailsDtoRequester']
---

# AccountRequestDetailsDtoRequester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.machine_account_creation_request.models.account_request_details_dto_requester import AccountRequestDetailsDtoRequester

account_request_details_dto_requester = AccountRequestDetailsDtoRequester(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

