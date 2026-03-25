---
id: v2026-create-privilege-criteria-request-groups-inner
title: CreatePrivilegeCriteriaRequestGroupsInner
pagination_label: CreatePrivilegeCriteriaRequestGroupsInner
sidebar_label: CreatePrivilegeCriteriaRequestGroupsInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreatePrivilegeCriteriaRequestGroupsInner', 'V2026CreatePrivilegeCriteriaRequestGroupsInner'] 
slug: /tools/sdk/python/v2026/models/create-privilege-criteria-request-groups-inner
tags: ['SDK', 'Software Development Kit', 'CreatePrivilegeCriteriaRequestGroupsInner', 'V2026CreatePrivilegeCriteriaRequestGroupsInner']
---

# CreatePrivilegeCriteriaRequestGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** |  **Enum** [  'AND',    'OR' ] | The logical operator to apply between criteria items in the group. | [optional] 
**criteria_items** | [**[]CreatePrivilegeCriteriaRequestGroupsInnerCriteriaItemsInner**](create-privilege-criteria-request-groups-inner-criteria-items-inner) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.create_privilege_criteria_request_groups_inner import CreatePrivilegeCriteriaRequestGroupsInner

create_privilege_criteria_request_groups_inner = CreatePrivilegeCriteriaRequestGroupsInner(
operator='AND',
criteria_items=[
                    sailpoint.v2026.models.create_privilege_criteria_request_groups_inner_criteria_items_inner.CreatePrivilegeCriteriaRequest_groups_inner_criteriaItems_inner(
                        target_type = 'group', 
                        operator = 'IN', 
                        values = [admin, superuser], 
                        ignore_case = True, )
                    ]
)

```
[[Back to top]](#) 

