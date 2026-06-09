---
id: requestonbehalfofconfig
title: Requestonbehalfofconfig
pagination_label: Requestonbehalfofconfig
sidebar_label: Requestonbehalfofconfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Requestonbehalfofconfig', 'Requestonbehalfofconfig'] 
slug: /tools/sdk/python/v1/models/requestonbehalfofconfig
tags: ['SDK', 'Software Development Kit', 'Requestonbehalfofconfig', 'Requestonbehalfofconfig']
---

# Requestonbehalfofconfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_request_on_behalf_of_anyone_by_anyone** | **bool** | If this is true, anyone can request access for anyone. | [optional] [default to False]
**allow_request_on_behalf_of_employee_by_manager** | **bool** | If this is true, a manager can request access for his or her direct reports. | [optional] [default to False]
}

## Example

```python
from sailpoint.access_requests_v1.models.requestonbehalfofconfig import Requestonbehalfofconfig

requestonbehalfofconfig = Requestonbehalfofconfig(
allow_request_on_behalf_of_anyone_by_anyone=True,
allow_request_on_behalf_of_employee_by_manager=True
)

```
[[Back to top]](#) 

