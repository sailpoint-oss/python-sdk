---
id: submit-users200-response
title: SubmitUsers200Response
pagination_label: SubmitUsers200Response
sidebar_label: SubmitUsers200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUsers200Response', 'SubmitUsers200Response'] 
slug: /tools/sdk/python//models/submit-users200-response
tags: ['SDK', 'Software Development Kit', 'SubmitUsers200Response', 'SubmitUsers200Response']
---

# SubmitUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**[]User**](user) |  | [optional] 
**info** | **str** |  | [optional] 
**job_status** | [**JobJobStatus**](job-job-status) |  | [optional] 
**status** | **int** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_users200_response import SubmitUsers200Response

submit_users200_response = SubmitUsers200Response(
users=[
                    sailpoint.nerm.models.user.User(
                        id = 'db6f8e8b-65c2-47d5-a0db-90bcc4e9df9e', 
                        uid = 'user1', 
                        name = 'myusername', 
                        email = 'test@sailpoint.com', 
                        type = 'NeprofileUser', 
                        title = 'Director', 
                        status = 'Active', 
                        login = 'myLogin', 
                        last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        cookies_accepted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        preferred_language = 'fr-CA', 
                        locale = 'fr-CA', 
                        group_strings = 'Admin_group, Developer_group', 
                        sailpoint_identity_id = '9496f8d6ddab49c0bef1e9ee6f1b835a', )
                    ],
info='job has started',
job_status=sailpoint.nerm.models.job_job_status.Job_job_status(
                    job_id = '3ce88e47ad6dba2ddf349d21', 
                    status = 'queued', ),
status=200
)

```
[[Back to top]](#) 

