---
id: applicationdiscoveryrequest
title: Applicationdiscoveryrequest
pagination_label: Applicationdiscoveryrequest
sidebar_label: Applicationdiscoveryrequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Applicationdiscoveryrequest', 'Applicationdiscoveryrequest'] 
slug: /tools/sdk/python/v1/models/applicationdiscoveryrequest
tags: ['SDK', 'Software Development Kit', 'Applicationdiscoveryrequest', 'Applicationdiscoveryrequest']
---

# Applicationdiscoveryrequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_ids** | **[]str** | List of dataset Ids to discover applications | [required]
}

## Example

```python
from sailpoint.application_discovery_v1.models.applicationdiscoveryrequest import Applicationdiscoveryrequest

applicationdiscoveryrequest = Applicationdiscoveryrequest(
dataset_ids=[
                    'source:datasetId12345'
                    ]
)

```
[[Back to top]](#) 

