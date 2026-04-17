---
id: form-attribute
title: FormAttribute
pagination_label: FormAttribute
sidebar_label: FormAttribute
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'FormAttribute', 'FormAttribute'] 
slug: /tools/sdk/python//models/form-attribute
tags: ['SDK', 'Software Development Kit', 'FormAttribute', 'FormAttribute']
---

# FormAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_id** | **str** | The id of the form | [optional] 
**ne_attribute_id** | **str** | The id of the attribute | [optional] 
**attr_type** |  **Enum** [  'ne_attribute',    'break' ] | The attribute type | [optional] 
**order** | **int** | The ordinal position of the attribute on the Form.  The order value determines the order or sequence the Form values are presented in the user interface. Each FormAttribute on a Form must have a unique order value. Order valuess can start at zero (0), but often start at one (1). The FormAttribute with order 1 is presented before the FormAttribute with order 2, and so on. Gaps in the order can exist and the system ignores them. | [optional] 
**id** | **str** | The id of the form attribute | [optional] 
**created_at** | **datetime** | The date-time the record created. | [optional] [readonly] 
**updated_at** | **datetime** | The date-time the record was last updated. | [optional] [readonly] 
}

## Example

```python
from sailpoint.nerm.models.form_attribute import FormAttribute

form_attribute = FormAttribute(
form_id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
ne_attribute_id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
attr_type='ne_attribute',
order=1,
id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
)

```
[[Back to top]](#) 

