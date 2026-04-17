---
id: get-attributes200-response
title: GetAttributes200Response
pagination_label: GetAttributes200Response
sidebar_label: GetAttributes200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetAttributes200Response', 'GetAttributes200Response'] 
slug: /tools/sdk/python//models/get-attributes200-response
tags: ['SDK', 'Software Development Kit', 'GetAttributes200Response', 'GetAttributes200Response']
---

# GetAttributes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ne_attributes** | [**[]Attribute**](attribute) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_attributes200_response import GetAttributes200Response

get_attributes200_response = GetAttributes200Response(
ne_attributes=[
                    sailpoint.nerm.models.attribute.Attribute(
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
                        type = 'AttachmentAttribute', )
                    ],
metadata=sailpoint.nerm.models.metadata.Metadata(
                    limit = 56, 
                    offset = 56, 
                    total = 56, 
                    next = '/endpoint?limit=10&offset=60', 
                    previous = '/endpoint?limit=10&offset=40', )
)

```
[[Back to top]](#) 

