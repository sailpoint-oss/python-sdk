---
id: v2025-common-access-item-request
title: CommonAccessItemRequest
pagination_label: CommonAccessItemRequest
sidebar_label: CommonAccessItemRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CommonAccessItemRequest', 'V2025CommonAccessItemRequest'] 
slug: /tools/sdk/python/v2025/models/common-access-item-request
tags: ['SDK', 'Software Development Kit', 'CommonAccessItemRequest', 'V2025CommonAccessItemRequest']
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
from sailpoint.v2025.models.common_access_item_request import CommonAccessItemRequest

common_access_item_request = CommonAccessItemRequest(
access=sailpoint.v2025.models.common_access_item_access.CommonAccessItemAccess(
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

