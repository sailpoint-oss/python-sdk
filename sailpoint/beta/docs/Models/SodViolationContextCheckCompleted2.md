---
id: beta-sod-violation-context-check-completed2
title: SodViolationContextCheckCompleted2
pagination_label: SodViolationContextCheckCompleted2
sidebar_label: SodViolationContextCheckCompleted2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SodViolationContextCheckCompleted2', 'BetaSodViolationContextCheckCompleted2'] 
slug: /tools/sdk/python/beta/models/sod-violation-context-check-completed2
tags: ['SDK', 'Software Development Kit', 'SodViolationContextCheckCompleted2', 'BetaSodViolationContextCheckCompleted2']
---

# SodViolationContextCheckCompleted2

An object referencing a completed SOD violation check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** |  **Enum** [  'SUCCESS',    'ERROR' ] | The status of SOD violation check | [optional] 
**uuid** | **str** | The id of the Violation check event | [optional] 
**violation_check_result** | [**SodViolationCheckResult2**](sod-violation-check-result2) |  | [optional] 
}

## Example

```python
from sailpoint.beta.models.sod_violation_context_check_completed2 import SodViolationContextCheckCompleted2

sod_violation_context_check_completed2 = SodViolationContextCheckCompleted2(
state='SUCCESS',
uuid='f73d16e9-a038-46c5-b217-1246e15fdbdd',
violation_check_result=sailpoint.beta.models.sod_violation_check_result.Sod Violation Check Result(
                    message = sailpoint.beta.models.error_message_dto.Error Message Dto(
                        locale = 'en-US', 
                        locale_origin = 'DEFAULT', 
                        text = 'The request was syntactically correct but its content is semantically invalid.', ), 
                    client_metadata = {requestedAppName=test-app, requestedAppId=2c91808f7892918f0178b78da4a305a1}, 
                    violation_contexts = [
                        sailpoint.beta.models.sod_violation_context.Sod Violation Context(
                            policy = sailpoint.beta.models.sod_policy_dto.Sod Policy Dto(
                                type = 'SOD_POLICY', 
                                id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde', 
                                name = 'Business SOD Policy', ), 
                            conflicting_access_criteria = sailpoint.beta.models.sod_violation_context_2_conflicting_access_criteria.SodViolationContext_2_conflictingAccessCriteria(
                                left_criteria = sailpoint.beta.models.sod_violation_context_2_conflicting_access_criteria_left_criteria.SodViolationContext_2_conflictingAccessCriteria_leftCriteria(
                                    criteria_list = [
                                        sailpoint.beta.models.sod_exempt_criteria.Sod Exempt Criteria(
                                            existing = True, 
                                            type = 'IDENTITY', 
                                            id = '2c918085771e9d3301773b3cb66f6398', 
                                            name = 'My HR Entitlement', )
                                        ], ), 
                                right_criteria = sailpoint.beta.models.sod_violation_context_2_conflicting_access_criteria_left_criteria.SodViolationContext_2_conflictingAccessCriteria_leftCriteria(), ), )
                        ], 
                    violated_policies = [
                        sailpoint.beta.models.sod_policy_dto.Sod Policy Dto(
                            id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde', 
                            name = 'Business SOD Policy', )
                        ], )
)

```
[[Back to top]](#) 

