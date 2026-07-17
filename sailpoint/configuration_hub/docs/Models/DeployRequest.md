---
id: deploy-request
title: DeployRequest
pagination_label: DeployRequest
sidebar_label: DeployRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DeployRequest', 'DeployRequest'] 
slug: /tools/sdk/python/configuration-hub/models/deploy-request
tags: ['SDK', 'Software Development Kit', 'DeployRequest', 'DeployRequest']
---

# DeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_id** | **str** | The id of the draft to be used by this deploy. | [required]
}

## Example

```python
from sailpoint.configuration_hub.models.deploy_request import DeployRequest

deploy_request = DeployRequest(
draft_id='3d0fe04b-57df-4a46-a83b-8f04b0f9d10b'
)

```
[[Back to top]](#) 

