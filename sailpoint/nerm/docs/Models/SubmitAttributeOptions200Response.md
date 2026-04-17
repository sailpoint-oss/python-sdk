---
id: submit-attribute-options200-response
title: SubmitAttributeOptions200Response
pagination_label: SubmitAttributeOptions200Response
sidebar_label: SubmitAttributeOptions200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitAttributeOptions200Response', 'SubmitAttributeOptions200Response'] 
slug: /tools/sdk/python//models/submit-attribute-options200-response
tags: ['SDK', 'Software Development Kit', 'SubmitAttributeOptions200Response', 'SubmitAttributeOptions200Response']
---

# SubmitAttributeOptions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ne_attribute_options** | [**[]AttributeOption**](attribute-option) |  | [optional] 
**info** | **str** |  | [optional] 
**job_status** | [**JobJobStatus**](job-job-status) |  | [optional] 
**status** | **int** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_attribute_options200_response import SubmitAttributeOptions200Response

submit_attribute_options200_response = SubmitAttributeOptions200Response(
ne_attribute_options=[
                    sailpoint.nerm.models.attribute_option.AttributeOption(
                        id = '', 
                        uid = '', 
                        ne_attribute_id = '', 
                        option = '', )
                    ],
info='job has started',
job_status=sailpoint.nerm.models.job_job_status.Job_job_status(
                    job_id = '3ce88e47ad6dba2ddf349d21', 
                    status = 'queued', ),
status=200
)

```
[[Back to top]](#) 

