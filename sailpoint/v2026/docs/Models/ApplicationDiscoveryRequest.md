---
id: v2026-application-discovery-request
title: ApplicationDiscoveryRequest
pagination_label: ApplicationDiscoveryRequest
sidebar_label: ApplicationDiscoveryRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApplicationDiscoveryRequest', 'V2026ApplicationDiscoveryRequest'] 
slug: /tools/sdk/python/v2026/models/application-discovery-request
tags: ['SDK', 'Software Development Kit', 'ApplicationDiscoveryRequest', 'V2026ApplicationDiscoveryRequest']
---

# ApplicationDiscoveryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_ids** | **[]str** | List of dataset Ids to discover applications | [required]
}

## Example

```python
from sailpoint.v2026.models.application_discovery_request import ApplicationDiscoveryRequest

application_discovery_request = ApplicationDiscoveryRequest(
dataset_ids=[
                    'source:datasetId12345'
                    ]
)

```
[[Back to top]](#) 

