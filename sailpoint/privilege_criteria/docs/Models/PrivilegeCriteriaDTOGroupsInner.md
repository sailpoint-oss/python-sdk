---
id: privilege-criteria-dto-groups-inner
title: PrivilegeCriteriaDTOGroupsInner
pagination_label: PrivilegeCriteriaDTOGroupsInner
sidebar_label: PrivilegeCriteriaDTOGroupsInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PrivilegeCriteriaDTOGroupsInner', 'PrivilegeCriteriaDTOGroupsInner'] 
slug: /tools/sdk/python/privilege-criteria/models/privilege-criteria-dto-groups-inner
tags: ['SDK', 'Software Development Kit', 'PrivilegeCriteriaDTOGroupsInner', 'PrivilegeCriteriaDTOGroupsInner']
---

# PrivilegeCriteriaDTOGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** |  **Enum** [  'AND',    'OR' ] | The logical operator to apply between criteria items in the group. | [optional] 
**criteria_items** | [**[]PrivilegeCriteriaDTOGroupsInnerCriteriaItemsInner**](privilege-criteria-dto-groups-inner-criteria-items-inner) |  | [optional] 
}

## Example

```python
from sailpoint.privilege_criteria.models.privilege_criteria_dto_groups_inner import PrivilegeCriteriaDTOGroupsInner

privilege_criteria_dto_groups_inner = PrivilegeCriteriaDTOGroupsInner(
operator='AND',
criteria_items=[
                    sailpoint.privilege_criteria.models.privilege_criteria_dto_groups_inner_criteria_items_inner.PrivilegeCriteriaDTO_groups_inner_criteriaItems_inner(
                        target_type = 'group', 
                        operator = 'IN', 
                        property = 'displayName', 
                        values = ["admin","superuser"], 
                        ignore_case = True, )
                    ]
)

```
[[Back to top]](#) 

