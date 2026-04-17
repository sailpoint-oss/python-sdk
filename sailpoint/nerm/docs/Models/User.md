---
id: user
title: User
pagination_label: User
sidebar_label: User
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'User', 'User'] 
slug: /tools/sdk/python//models/user
tags: ['SDK', 'Software Development Kit', 'User', 'User']
---

# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the object to retrieve or update | [optional] 
**uid** | **str** | UID of the user | [optional] 
**name** | **str** | The name | [optional] 
**email** | **str** | The email | [optional] 
**type** |  **Enum** [  'NeprofileUser',    'NeaccessUser' ] | Type of user | [optional] [default to 'NeprofileUser']
**title** | **str** | The title | [optional] 
**status** |  **Enum** [  'Active',    'Pending',    'Disabled' ] | Status of the user | [optional] 
**login** | **str** | The login | [optional] 
**last_login** | **datetime** | When the user last logged in | [optional] [readonly] 
**cookies_accepted_at** | **datetime** | When cookies were accepted | [optional] [readonly] 
**preferred_language** | **str** | The locale the user prefers to use | [optional] 
**locale** | **str** | The locale the user prefers to use | [optional] 
**group_strings** | **str** | Group strings configured on the customer's Active Directory configuration, provided by the IDP at the moment on authentication. | [optional] 
**sailpoint_identity_id** | **str** | The identity ID of the user in ISC | [optional] 
}

## Example

```python
from sailpoint.nerm.models.user import User

user = User(
id='db6f8e8b-65c2-47d5-a0db-90bcc4e9df9e',
uid='user1',
name='myusername',
email='test@sailpoint.com',
type='NeprofileUser',
title='Director',
status='Active',
login='myLogin',
last_login=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
cookies_accepted_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
preferred_language='fr-CA',
locale='fr-CA',
group_strings='Admin_group, Developer_group',
sailpoint_identity_id='9496f8d6ddab49c0bef1e9ee6f1b835a'
)

```
[[Back to top]](#) 

