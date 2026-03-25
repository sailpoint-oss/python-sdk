---
id: v2026-privilege-criteria-dto-groups-inner-criteria-items-inner
title: PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner
pagination_label: PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner
sidebar_label: PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner', 'V2026PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner'] 
slug: /tools/sdk/python/v2026/models/privilege-criteria-dto-groups-inner-criteria-items-inner
tags: ['SDK', 'Software Development Kit', 'PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner', 'V2026PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner']
---

# PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** |  **Enum** [  'group' ] | The target type for the criteria item. | [optional] 
**operator** |  **Enum** [  'IN',    'EQUALS',    'NOT_EQUALS',    'CONTAINS',    'DOES_NOT_CONTAIN',    'STARTS_WITH',    'ENDS_WITH' ] | The operator to apply to the property and values. | [optional] 
**var_property** | **str** |  | [optional] 
**values** | **[]str** | The values to evaluate the property against. | [optional] 
**ignore_case** | **bool** | Whether to ignore case when evaluating the property against the values. | [optional] [default to False]
}

## Example

```python
from sailpoint.v2026.models.privilege_criteria_dto_groups_inner_criteria_items_inner import PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner

privilege_criteria_dto_groups_inner_criteria_items_inner = PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner(
target_type='group',
operator='IN',
var_property='',
values=[admin, superuser],
ignore_case=True
)

```
[[Back to top]](#) 

