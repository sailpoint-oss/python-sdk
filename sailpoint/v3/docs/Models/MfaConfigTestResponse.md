---
id: mfa-config-test-response
title: MfaConfigTestResponse
pagination_label: MfaConfigTestResponse
sidebar_label: MfaConfigTestResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MfaConfigTestResponse', 'MfaConfigTestResponse'] 
slug: /tools/sdk/python/v3/models/mfa-config-test-response
tags: ['SDK', 'Software Development Kit', 'MfaConfigTestResponse', 'MfaConfigTestResponse']
---

# MfaConfigTestResponse

Response model for configuration test of a given MFA method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** |  **Enum** [  'SUCCESS',    'FAILED' ] | The configuration test result. | [optional] [readonly] 
**error** | **str** | The error message to indicate the failure of configuration test. | [optional] [readonly] 
}

## Example

```python
from sailpoint.v3.models.mfa_config_test_response import MfaConfigTestResponse

mfa_config_test_response = MfaConfigTestResponse(
state='SUCCESS',
error='MFA Method is disabled.'
)

```
[[Back to top]](#) 

