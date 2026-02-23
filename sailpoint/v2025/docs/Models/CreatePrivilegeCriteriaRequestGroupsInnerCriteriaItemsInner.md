---
id: v2025-create-privilege-criteria-request-groups-inner-criteria-items-inner
title: CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner
pagination_label: CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner
sidebar_label: CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner', 'V2025CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner'] 
slug: /tools/sdk/python/v2025/models/create-privilege-criteria-request-groups-inner-criteria-items-inner
tags: ['SDK', 'Software Development Kit', 'CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner', 'V2025CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner']
---

# CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** |  **Enum** [  'group' ] | The target type of the criteria item. | [optional] 
**operator** |  **Enum** [  'IN',    'EQUALS',    'NOT_EQUALS',    'CONTAINS',    'DOES_NOT_CONTAIN',    'STARTS_WITH',    'ENDS_WITH' ] |  | [optional] 
**values** | **[]str** | The values to evaluate the property against. | [optional] 
**ignore_case** | **bool** | Whether to ignore case when evaluating the property against the values. | [optional] [default to False]
}

## Example

```python
from sailpoint.v2025.models.create_privilege_criteria_request_groups_inner_criteria_items_inner import CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner

create_privilege_criteria_request_groups_inner_criteria_items_inner = CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner(
target_type='group',
operator='IN',
values=[admin, superuser],
ignore_case=True
)

```
[[Back to top]](#) 

