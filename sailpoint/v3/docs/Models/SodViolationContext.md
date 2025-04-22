---
id: sod-violation-context
title: SodViolationContext
pagination_label: SodViolationContext
sidebar_label: SodViolationContext
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SodViolationContext', 'SodViolationContext'] 
slug: /tools/sdk/python/v3/models/sod-violation-context
tags: ['SDK', 'Software Development Kit', 'SodViolationContext', 'SodViolationContext']
---

# SodViolationContext

The contextual information of the violated criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**SodPolicyDto**](sod-policy-dto) |  | [optional] 
**conflicting_access_criteria** | [**SodViolationContextConflictingAccessCriteria**](sod-violation-context-conflicting-access-criteria) |  | [optional] 
}

## Example

```python
from sailpoint.v3.models.sod_violation_context import SodViolationContext

sod_violation_context = SodViolationContext(
policy=sailpoint.v3.models.sod_policy_dto.SodPolicyDto(
                    type = 'SOD_POLICY', 
                    id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde', 
                    name = 'Business SOD Policy', ),
conflicting_access_criteria=sailpoint.v3.models.sod_violation_context_conflicting_access_criteria.SodViolationContext_conflictingAccessCriteria(
                    left_criteria = sailpoint.v3.models.sod_violation_context_conflicting_access_criteria_left_criteria.SodViolationContext_conflictingAccessCriteria_leftCriteria(
                        criteria_list = [
                            sailpoint.v3.models.sod_exempt_criteria.SodExemptCriteria(
                                existing = True, 
                                type = 'IDENTITY', 
                                id = '2c918085771e9d3301773b3cb66f6398', 
                                name = 'My HR Entitlement', )
                            ], ), 
                    right_criteria = sailpoint.v3.models.sod_violation_context_conflicting_access_criteria_left_criteria.SodViolationContext_conflictingAccessCriteria_leftCriteria(), )
)

```
[[Back to top]](#) 

