---
id: create-attribute-request
title: CreateAttributeRequest
pagination_label: CreateAttributeRequest
sidebar_label: CreateAttributeRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateAttributeRequest', 'CreateAttributeRequest'] 
slug: /tools/sdk/python//models/create-attribute-request
tags: ['SDK', 'Software Development Kit', 'CreateAttributeRequest', 'CreateAttributeRequest']
---

# CreateAttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ne_attribute** | [**Attribute1**](attribute1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_attribute_request import CreateAttributeRequest

create_attribute_request = CreateAttributeRequest(
ne_attribute=sailpoint.nerm.models.attribute_1.Attribute_1(
                    id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    uid = 'myattribute', 
                    label = 'birthday', 
                    description = 'Your birthday', 
                    tool_tip = 'Put your birthday here mm-dd-yyyy', 
                    archived = False, 
                    date_format = 'mm/dd/yyyy', 
                    selectable_status = 'Active', 
                    risk_type = 'OverallRisk', 
                    ownership_driven = True, 
                    allow_multiple_selections = True, 
                    filtered_by_ne_attribute = True, 
                    filtering_ne_attribute_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    ne_attribute_filter_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    reverse_association_attribute = sailpoint.nerm.models.attribute_properties.AttributeProperties(
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
                    profile_type_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    data_type = 'text field', 
                    type = 'AttachmentAttribute', 
                    validations_attributes = sailpoint.nerm.models.attribute_1_validations_attributes.Attribute_1_validations_attributes(
                        validation_method = 'required', 
                        value = 'mm-dd-yyyy', 
                        _destroy = False, ), )
)

```
[[Back to top]](#) 

