---
id: beta-sod-violation-context2-conflicting-access-criteria
title: SodViolationContext2ConflictingAccessCriteria
pagination_label: SodViolationContext2ConflictingAccessCriteria
sidebar_label: SodViolationContext2ConflictingAccessCriteria
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SodViolationContext2ConflictingAccessCriteria', 'BetaSodViolationContext2ConflictingAccessCriteria'] 
slug: /tools/sdk/python/beta/models/sod-violation-context2-conflicting-access-criteria
tags: ['SDK', 'Software Development Kit', 'SodViolationContext2ConflictingAccessCriteria', 'BetaSodViolationContext2ConflictingAccessCriteria']
---

# SodViolationContext2ConflictingAccessCriteria

The object which contains the left and right hand side of the entitlements that got violated according to the policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_criteria** | [**SodViolationContext2ConflictingAccessCriteriaLeftCriteria**](sod-violation-context2-conflicting-access-criteria-left-criteria) |  | [optional] 
**right_criteria** | [**SodViolationContext2ConflictingAccessCriteriaLeftCriteria**](sod-violation-context2-conflicting-access-criteria-left-criteria) |  | [optional] 
}

## Example

```python
from sailpoint.beta.models.sod_violation_context2_conflicting_access_criteria import SodViolationContext2ConflictingAccessCriteria

sod_violation_context2_conflicting_access_criteria = SodViolationContext2ConflictingAccessCriteria(
left_criteria=sailpoint.beta.models.sod_violation_context_2_conflicting_access_criteria_left_criteria.SodViolationContext_2_conflictingAccessCriteria_leftCriteria(
                    criteria_list = [
                        sailpoint.beta.models.sod_exempt_criteria.Sod Exempt Criteria(
                            existing = True, 
                            type = 'IDENTITY', 
                            id = '2c918085771e9d3301773b3cb66f6398', 
                            name = 'My HR Entitlement', )
                        ], ),
right_criteria=sailpoint.beta.models.sod_violation_context_2_conflicting_access_criteria_left_criteria.SodViolationContext_2_conflictingAccessCriteria_leftCriteria(
                    criteria_list = [
                        sailpoint.beta.models.sod_exempt_criteria.Sod Exempt Criteria(
                            existing = True, 
                            type = 'IDENTITY', 
                            id = '2c918085771e9d3301773b3cb66f6398', 
                            name = 'My HR Entitlement', )
                        ], )
)

```
[[Back to top]](#) 

