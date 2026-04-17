---
id: delegator-user
title: DelegatorUser
pagination_label: DelegatorUser
sidebar_label: DelegatorUser
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DelegatorUser', 'DelegatorUser'] 
slug: /tools/sdk/python//models/delegator-user
tags: ['SDK', 'Software Development Kit', 'DelegatorUser', 'DelegatorUser']
---

# DelegatorUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the delegator user | [optional] 
**uid** | **str** | The uid of the delegator user | [optional] 
**type** | **str** | The type of the delegator user | [optional] 
**name** | **str** | The name of the delegator user | [optional] 
**email** | **str** | The email of the delegator user | [optional] 
**status** | **str** | The status of the delegator user | [optional] 
**login** | **str** | The login of the delegator user | [optional] 
**last_login** | **datetime** | The last login timestamp of the delegator user | [optional] 
**created_at** | **datetime** | The date-time the record created. | [optional] [readonly] 
**updated_at** | **datetime** | The date-time the record was last updated. | [optional] [readonly] 
}

## Example

```python
from sailpoint.nerm.v2025.models.delegator_user import DelegatorUser

delegator_user = DelegatorUser(
id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
uid='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
type='NeprofileUser',
name='Jane Doe',
email='jane@example.com',
status='active',
login='jane.doe',
last_login='2024-06-01T12:34:56Z',
created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
)

```
[[Back to top]](#) 

