---
id: v2024-email-status-dto
title: EmailStatusDto
pagination_label: EmailStatusDto
sidebar_label: EmailStatusDto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EmailStatusDto', 'V2024EmailStatusDto'] 
slug: /tools/sdk/python/v2024/models/email-status-dto
tags: ['SDK', 'Software Development Kit', 'EmailStatusDto', 'V2024EmailStatusDto']
---

# EmailStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the verified sender address | [optional] 
**email** | **str** | The verified sender email address | [optional] 
**is_verified_by_domain** | **bool** | Whether the sender address is verified by domain | [optional] [default to False]
**verification_status** |  **Enum** [  'PENDING',    'SUCCESS',    'FAILED',    'NA' ] | The verification status of the sender address | [optional] 
**region** | **str** | The AWS SES region the sender address is associated with | [optional] 
}

## Example

```python
from sailpoint.v2024.models.email_status_dto import EmailStatusDto

email_status_dto = EmailStatusDto(
id='',
email='sender@example.com',
is_verified_by_domain=False,
verification_status='SUCCESS',
region='us-east-1'
)

```
[[Back to top]](#) 

