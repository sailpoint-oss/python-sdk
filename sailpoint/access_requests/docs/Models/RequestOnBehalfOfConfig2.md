---
id: request-on-behalf-of-config2
title: RequestOnBehalfOfConfig2
pagination_label: RequestOnBehalfOfConfig2
sidebar_label: RequestOnBehalfOfConfig2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RequestOnBehalfOfConfig2', 'RequestOnBehalfOfConfig2'] 
slug: /tools/sdk/python/access-requests/models/request-on-behalf-of-config2
tags: ['SDK', 'Software Development Kit', 'RequestOnBehalfOfConfig2', 'RequestOnBehalfOfConfig2']
---

# RequestOnBehalfOfConfig2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_request_on_behalf_of_anyone_by_anyone** | **bool** | If this is true, anyone can request access for anyone. | [optional] [default to False]
**allow_request_on_behalf_of_employee_by_manager** | **bool** | If this is true, a manager can request access for his or her direct reports. | [optional] [default to False]
}

## Example

```python
from sailpoint.access_requests.models.request_on_behalf_of_config2 import RequestOnBehalfOfConfig2

request_on_behalf_of_config2 = RequestOnBehalfOfConfig2(
allow_request_on_behalf_of_anyone_by_anyone=True,
allow_request_on_behalf_of_employee_by_manager=True
)

```
[[Back to top]](#) 

