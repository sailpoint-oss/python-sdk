---
id: beta-slim-discovered-applications
title: SlimDiscoveredApplications
pagination_label: SlimDiscoveredApplications
sidebar_label: SlimDiscoveredApplications
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SlimDiscoveredApplications', 'BetaSlimDiscoveredApplications'] 
slug: /tools/sdk/python/beta/models/slim-discovered-applications
tags: ['SDK', 'Software Development Kit', 'SlimDiscoveredApplications', 'BetaSlimDiscoveredApplications']
---

# SlimDiscoveredApplications

Discovered applications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the discovered application. | [optional] 
**name** | **str** | Name of the discovered application. | [optional] 
**discovery_source** | **str** | Source from which the application was discovered. | [optional] 
**discovered_vendor** | **str** | The vendor associated with the discovered application. | [optional] 
**description** | **str** | A brief description of the discovered application. | [optional] 
**recommended_connectors** | **[]str** | List of recommended connectors for the application. | [optional] 
**discovered_at** | **datetime** | The timestamp when the application was last received via an entitlement aggregation invocation  or a manual csv upload, in ISO 8601 format. | [optional] 
**created_at** | **datetime** | The timestamp when the application was first discovered, in ISO 8601 format. | [optional] 
**status** | **str** | The status of an application within the discovery source.  By default this field is set to \"ACTIVE\" when the application is discovered.  If an application has been deleted from within the discovery source, the status will be set to \"INACTIVE\". | [optional] 
**risk_score** | **int** | The risk score of the application ranging from 0-100, 100 being highest risk. | [optional] 
**is_business** | **bool** | Indicates whether the application is used for business purposes. | [optional] [default to True]
**total_signins_count** | **int** | The total number of sign-in accounts for the application. | [optional] 
**risk_level** |  **Enum** [  'High',    'Medium',    'Low' ] | The risk level of the application. | [optional] 
}

## Example

```python
from sailpoint.beta.models.slim_discovered_applications import SlimDiscoveredApplications

slim_discovered_applications = SlimDiscoveredApplications(
id='',
name='ExampleApp',
discovery_source='csv',
discovered_vendor='ExampleVendor',
description='An application for managing examples.',
recommended_connectors=[ConnectorA, ConnectorB],
discovered_at='2023-01-01T12:00Z',
created_at='2023-01-01T12:00Z',
status='ACTIVE',
risk_score=1,
is_business=False,
total_signins_count=1,
risk_level='Low'
)

```
[[Back to top]](#) 

