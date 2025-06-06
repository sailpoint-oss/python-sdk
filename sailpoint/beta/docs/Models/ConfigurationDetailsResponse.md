---
id: beta-configuration-details-response
title: ConfigurationDetailsResponse
pagination_label: ConfigurationDetailsResponse
sidebar_label: ConfigurationDetailsResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ConfigurationDetailsResponse', 'BetaConfigurationDetailsResponse'] 
slug: /tools/sdk/python/beta/models/configuration-details-response
tags: ['SDK', 'Software Development Kit', 'ConfigurationDetailsResponse', 'BetaConfigurationDetailsResponse']
---

# ConfigurationDetailsResponse

The request body of Reassignment Configuration Details for a specific identity and config type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_type** | [**ConfigTypeEnum**](config-type-enum) |  | [optional] 
**target_identity** | [**Identity1**](identity1) |  | [optional] 
**start_date** | **datetime** | The date from which to start reassigning work items | [optional] 
**end_date** | **datetime** | The date from which to stop reassigning work items.  If this is an empty string it indicates a permanent reassignment. | [optional] 
**audit_details** | [**AuditDetails**](audit-details) |  | [optional] 
}

## Example

```python
from sailpoint.beta.models.configuration_details_response import ConfigurationDetailsResponse

configuration_details_response = ConfigurationDetailsResponse(
config_type='ACCESS_REQUESTS',
target_identity=sailpoint.beta.models.identity_1.Identity_1(
                    id = '2c91808380aa05580180aaaaf1940410', 
                    name = 'William Wilson', ),
start_date='2022-07-21T11:13:12.345Z',
end_date='0001-01-01T00:00Z',
audit_details=sailpoint.beta.models.audit_details.AuditDetails(
                    created = '2022-07-21T11:13:12.345Z', 
                    created_by = sailpoint.beta.models.identity_1.Identity_1(
                        id = '2c91808380aa05580180aaaaf1940410', 
                        name = 'William Wilson', ), 
                    modified = '2022-07-21T11:13:12.345Z', 
                    modified_by = sailpoint.beta.models.identity_1.Identity_1(
                        id = '2c91808380aa05580180aaaaf1940410', 
                        name = 'William Wilson', ), )
)

```
[[Back to top]](#) 

