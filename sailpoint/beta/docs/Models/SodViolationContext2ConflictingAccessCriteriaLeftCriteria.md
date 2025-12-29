---
id: beta-sod-violation-context2-conflicting-access-criteria-left-criteria
title: SodViolationContext2ConflictingAccessCriteriaLeftCriteria
pagination_label: SodViolationContext2ConflictingAccessCriteriaLeftCriteria
sidebar_label: SodViolationContext2ConflictingAccessCriteriaLeftCriteria
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SodViolationContext2ConflictingAccessCriteriaLeftCriteria', 'BetaSodViolationContext2ConflictingAccessCriteriaLeftCriteria'] 
slug: /tools/sdk/python/beta/models/sod-violation-context2-conflicting-access-criteria-left-criteria
tags: ['SDK', 'Software Development Kit', 'SodViolationContext2ConflictingAccessCriteriaLeftCriteria', 'BetaSodViolationContext2ConflictingAccessCriteriaLeftCriteria']
---

# SodViolationContext2ConflictingAccessCriteriaLeftCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria_list** | [**[]SodExemptCriteria2**](sod-exempt-criteria2) |  | [optional] 
}

## Example

```python
from sailpoint.beta.models.sod_violation_context2_conflicting_access_criteria_left_criteria import SodViolationContext2ConflictingAccessCriteriaLeftCriteria

sod_violation_context2_conflicting_access_criteria_left_criteria = SodViolationContext2ConflictingAccessCriteriaLeftCriteria(
criteria_list=[
                    sailpoint.beta.models.sod_exempt_criteria.Sod Exempt Criteria(
                        existing = True, 
                        type = 'IDENTITY', 
                        id = '2c918085771e9d3301773b3cb66f6398', 
                        name = 'My HR Entitlement', )
                    ]
)

```
[[Back to top]](#) 

