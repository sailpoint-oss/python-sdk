---
id: manual-discover-applications
title: ManualDiscoverApplications
pagination_label: ManualDiscoverApplications
sidebar_label: ManualDiscoverApplications
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ManualDiscoverApplications', 'ManualDiscoverApplications'] 
slug: /tools/sdk/python/application-discovery/models/manual-discover-applications
tags: ['SDK', 'Software Development Kit', 'ManualDiscoverApplications', 'ManualDiscoverApplications']
---

# ManualDiscoverApplications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | The CSV file to upload containing `application_name` and `description` columns. Each row represents an application to be discovered. | [required]
}

## Example

```python
from sailpoint.application_discovery.models.manual_discover_applications import ManualDiscoverApplications

manual_discover_applications = ManualDiscoverApplications(
file='[B@54a3ab8f'
)

```
[[Back to top]](#) 

