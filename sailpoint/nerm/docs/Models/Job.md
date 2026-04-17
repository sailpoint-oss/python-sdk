---
id: job
title: Job
pagination_label: Job
sidebar_label: Job
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Job', 'Job'] 
slug: /tools/sdk/python//models/job
tags: ['SDK', 'Software Development Kit', 'Job', 'Job']
---

# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **str** |  | [optional] 
**job_status** | [**JobJobStatus**](job-job-status) |  | [optional] 
**status** | **int** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.job import Job

job = Job(
info='job has started',
job_status=sailpoint.nerm.models.job_job_status.Job_job_status(
                    job_id = '3ce88e47ad6dba2ddf349d21', 
                    status = 'queued', ),
status=200
)

```
[[Back to top]](#) 

