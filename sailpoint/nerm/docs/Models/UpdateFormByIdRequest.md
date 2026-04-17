---
id: update-form-by-id-request
title: UpdateFormByIdRequest
pagination_label: UpdateFormByIdRequest
sidebar_label: UpdateFormByIdRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UpdateFormByIdRequest', 'UpdateFormByIdRequest'] 
slug: /tools/sdk/python//models/update-form-by-id-request
tags: ['SDK', 'Software Development Kit', 'UpdateFormByIdRequest', 'UpdateFormByIdRequest']
---

# UpdateFormByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**Form1**](form1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.update_form_by_id_request import UpdateFormByIdRequest

update_form_by_id_request = UpdateFormByIdRequest(
role=sailpoint.nerm.models.form_1.Form_1(
                    uid = 'form_uid', 
                    description = 'Form for creating new profile', 
                    name = 'My Form Name', 
                    archived = False, )
)

```
[[Back to top]](#) 

