---
id: v2026-common-access-id-status
title: CommonAccessIDStatus
pagination_label: CommonAccessIDStatus
sidebar_label: CommonAccessIDStatus
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CommonAccessIDStatus', 'V2026CommonAccessIDStatus'] 
slug: /tools/sdk/python/v2026/models/common-access-id-status
tags: ['SDK', 'Software Development Kit', 'CommonAccessIDStatus', 'V2026CommonAccessIDStatus']
---

# CommonAccessIDStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_ids** | **[]str** | List of confirmed common access ids. | [optional] 
**denied_ids** | **[]str** | List of denied common access ids. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.common_access_id_status import CommonAccessIDStatus

common_access_id_status = CommonAccessIDStatus(
confirmed_ids=[
                    ''
                    ],
denied_ids=[
                    ''
                    ]
)

```
[[Back to top]](#) 

