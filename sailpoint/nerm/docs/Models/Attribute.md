---
id: attribute
title: Attribute
pagination_label: Attribute
sidebar_label: Attribute
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Attribute', 'Attribute'] 
slug: /tools/sdk/python//models/attribute
tags: ['SDK', 'Software Development Kit', 'Attribute', 'Attribute']
---

# Attribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the attribute | [optional] [readonly] 
**uid** | **str** | The user-specified identifier of the attribute | [optional] [readonly] 
**label** | **str** | The label for the attribute | [optional] 
**description** | **str** | A description of the attribute | [optional] 
**tool_tip** | **str** | The helper text that accompanies the attribute | [optional] 
**crypt** | **bool** | Whether the attribute is encrypted | [optional] 
**archived** | **bool** | Whether the attribute is archived | [optional] 
**archived_on** | **datetime** | When the attribute was archived | [optional] 
**created_at** | **datetime** | When the attribute was created | [optional] 
**updated_at** | **datetime** | When the attribute was updated | [optional] 
**date_format** |  **Enum** [  'mm/dd/yyyy',    'mm-dd-yyyy',    'dd/mm/yyyy',    'dd-mm-yyyy',    'yyyy/mm/dd',    'yyyy-mm-dd' ] | The format of the date input if it is a date input | [optional] 
**selectable_status** | **str** | The status of the profiles that can be selected | [optional] 
**risk_type** | **str** | Type of risk that applies to the attribute | [optional] 
**ownership_driven** | **bool** | Only shows profiles that the user currently has access to, to be selected | [optional] 
**allow_multiple_selections** | **bool** | Whether or not multiple selections can be made on something like a contributor search. | [optional] 
**filtered_by_ne_attribute** | **bool** | Whether or not the attribute is filtered by another attribute | [optional] 
**filtering_ne_attribute_id** | **str** | The ID of the filtering attribute | [optional] 
**ne_attribute_filter_id** | **str** | The ID of the attribute filter | [optional] 
**reverse_association_attribute** | [**AttributeProperties**](attribute-properties) |  | [optional] 
**profile_type_id** | **str** | The ID of the profile type the attribute applies to | [optional] 
**data_type** |  **Enum** [  'text field',    'text area',    'drop-down',    'radio buttons',    'check boxes',    'date',    'tags',    'attachment',    'profile select',    'profile search',    'owner select',    'owner search',    'contributor select',    'contributor search' ] | The type of data that applies to the attribute | [optional] 
**type** |  **Enum** [  'AttachmentAttribute',    'CheckBoxesAttribute',    'ContributorSearchAttribute',    'ContributorSelectAttribute',    'DateAttribute',    'DropDownAttribute',    'OwnerSearchAttribute',    'OwnerSelectAttribute',    'ProfileSearchAttribute',    'ProfileSelectAttribute',    'RadioButtonsAttribute',    'TagsAttribute',    'TextAreaAttribute',    'TextFieldAttribute' ] | The attribute's type | [optional] 
}

## Example

```python
from sailpoint.nerm.models.attribute import Attribute

attribute = Attribute(
id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
uid='myattribute',
label='birthday',
description='Your birthday',
tool_tip='Put your birthday here mm-dd-yyyy',
crypt=False,
archived=False,
archived_on=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
date_format='mm/dd/yyyy',
selectable_status='Active',
risk_type='OverallRisk',
ownership_driven=True,
allow_multiple_selections=True,
filtered_by_ne_attribute=True,
filtering_ne_attribute_id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
ne_attribute_filter_id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
reverse_association_attribute=sailpoint.nerm.models.attribute_properties.AttributeProperties(
                    id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    uid = 'myattribute', 
                    label = 'birthday', 
                    description = 'Your birthday', 
                    tool_tip = 'Put your birthday here mm-dd-yyyy', 
                    crypt = False, 
                    archived = False, 
                    archived_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    date_format = 'mm/dd/yyyy', 
                    selectable_status = 'Active', 
                    risk_score_setting = 'standard', 
                    risk_type = 'OverallRisk', 
                    ownership_driven = True, 
                    allow_multiple_selections = True, 
                    filtered_by_ne_attribute = True, 
                    filtering_ne_attribute_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    ne_attribute_filter_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    reverse_association_attribute_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    profile_type_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    legacy_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    tmp_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    tmp_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
profile_type_id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
data_type='text field',
type='AttachmentAttribute'
)

```
[[Back to top]](#) 

