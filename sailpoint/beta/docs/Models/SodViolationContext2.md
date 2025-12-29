---
id: beta-sod-violation-context2
title: SodViolationContext2
pagination_label: SodViolationContext2
sidebar_label: SodViolationContext2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SodViolationContext2', 'BetaSodViolationContext2'] 
slug: /tools/sdk/python/beta/models/sod-violation-context2
tags: ['SDK', 'Software Development Kit', 'SodViolationContext2', 'BetaSodViolationContext2']
---

# SodViolationContext2

The contextual information of the violated criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**SodPolicyDto1**](sod-policy-dto1) |  | [optional] 
**conflicting_access_criteria** | [**SodViolationContext2ConflictingAccessCriteria**](sod-violation-context2-conflicting-access-criteria) |  | [optional] 
}

## Example

```python
from sailpoint.beta.models.sod_violation_context2 import SodViolationContext2

sod_violation_context2 = SodViolationContext2(
policy=sailpoint.beta.models.sod_policy_dto.Sod Policy Dto(
                    type = 'SOD_POLICY', 
                    id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde', 
                    name = 'Business SOD Policy', ),
conflicting_access_criteria=sailpoint.beta.models.sod_violation_context_2_conflicting_access_criteria.SodViolationContext_2_conflictingAccessCriteria(
                    left_criteria = sailpoint.beta.models.sod_violation_context_2_conflicting_access_criteria_left_criteria.SodViolationContext_2_conflictingAccessCriteria_leftCriteria(
                        criteria_list = [
                            sailpoint.beta.models.sod_exempt_criteria.Sod Exempt Criteria(
                                existing = True, 
                                type = 'IDENTITY', 
                                id = '2c918085771e9d3301773b3cb66f6398', 
                                name = 'My HR Entitlement', )
                            ], ), 
                    right_criteria = sailpoint.beta.models.sod_violation_context_2_conflicting_access_criteria_left_criteria.SodViolationContext_2_conflictingAccessCriteria_leftCriteria(), )
)

```
[[Back to top]](#) 

