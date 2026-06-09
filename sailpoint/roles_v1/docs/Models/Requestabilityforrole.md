---
id: requestabilityforrole
title: Requestabilityforrole
pagination_label: Requestabilityforrole
sidebar_label: Requestabilityforrole
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Requestabilityforrole', 'Requestabilityforrole'] 
slug: /tools/sdk/python/v1/models/requestabilityforrole
tags: ['SDK', 'Software Development Kit', 'Requestabilityforrole', 'Requestabilityforrole']
---

# Requestabilityforrole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments_required** | **bool** | Whether the requester of the containing object must provide comments justifying the request | [optional] [default to False]
**denial_comments_required** | **bool** | Whether an approver must provide comments when denying the request | [optional] [default to False]
**reauthorization_required** | **bool** | Indicates whether reauthorization is required for the request. | [optional] [default to False]
**require_end_date** | **bool** | Indicates whether the requester of the containing object must provide access end date. | [optional] [default to False]
**max_permitted_access_duration** | [**Accessduration**](accessduration) |  | [optional] 
**approval_schemes** | [**[]Approvalschemeforrole**](approvalschemeforrole) | List describing the steps in approving the request | [optional] 
**dimension_schema** | [**Dimensionschema**](dimensionschema) |  | [optional] 
}

## Example

```python
from sailpoint.roles_v1.models.requestabilityforrole import Requestabilityforrole

requestabilityforrole = Requestabilityforrole(
comments_required=True,
denial_comments_required=True,
reauthorization_required=True,
require_end_date=True,
max_permitted_access_duration=sailpoint.roles_v1.models.accessduration.accessduration(
                    value = 6, 
                    time_unit = 'MONTHS', ),
approval_schemes=[
                    sailpoint.roles_v1.models.approvalschemeforrole.approvalschemeforrole(
                        approver_type = 'GOVERNANCE_GROUP', 
                        approver_id = '46c79819-a69f-49a2-becb-12c971ae66c6', )
                    ],
dimension_schema=sailpoint.roles_v1.models.dimensionschema.dimensionschema(
                    dimension_attributes = [
                        sailpoint.roles_v1.models.dimensionattribute.dimensionattribute(
                            name = 'city', 
                            display_name = 'City', 
                            derived = True, )
                        ], )
)

```
[[Back to top]](#) 

