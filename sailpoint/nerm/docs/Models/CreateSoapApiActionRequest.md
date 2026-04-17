---
id: create-soap-api-action-request
title: CreateSoapApiActionRequest
pagination_label: CreateSoapApiActionRequest
sidebar_label: CreateSoapApiActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateSoapApiActionRequest', 'CreateSoapApiActionRequest'] 
slug: /tools/sdk/python//models/create-soap-api-action-request
tags: ['SDK', 'Software Development Kit', 'CreateSoapApiActionRequest', 'CreateSoapApiActionRequest']
---

# CreateSoapApiActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**SoapApiAction**](soap-api-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_soap_api_action_request import CreateSoapApiActionRequest

create_soap_api_action_request = CreateSoapApiActionRequest(
workflow_action=sailpoint.nerm.models.soap_api_action.SoapApiAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Makes a request to a SOAP API.', 
                    archived = False, )
)

```
[[Back to top]](#) 

