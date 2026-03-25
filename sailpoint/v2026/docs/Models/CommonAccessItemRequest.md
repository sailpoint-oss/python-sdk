---
id: v2026-common-access-item-request
title: CommonAccessItemRequest
pagination_label: CommonAccessItemRequest
sidebar_label: CommonAccessItemRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CommonAccessItemRequest', 'V2026CommonAccessItemRequest'] 
slug: /tools/sdk/python/v2026/models/common-access-item-request
tags: ['SDK', 'Software Development Kit', 'CommonAccessItemRequest', 'V2026CommonAccessItemRequest']
---

# CommonAccessItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**CommonAccessItemAccess**](common-access-item-access) |  | [optional] 
**status** | [**CommonAccessItemState**](common-access-item-state) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.common_access_item_request import CommonAccessItemRequest

common_access_item_request = CommonAccessItemRequest(
access=sailpoint.v2026.models.common_access_item_access.Common Access Item Access(
                    id = '', 
                    type = 'ACCESS_PROFILE', 
                    name = '', 
                    description = '', 
                    owner_name = '', 
                    owner_id = '', ),
status='CONFIRMED'
)

```
[[Back to top]](#) 

