---
id: form-instance-recipient
title: FormInstanceRecipient
pagination_label: FormInstanceRecipient
sidebar_label: FormInstanceRecipient
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'FormInstanceRecipient', 'FormInstanceRecipient'] 
slug: /tools/sdk/python/custom-forms/models/form-instance-recipient
tags: ['SDK', 'Software Development Kit', 'FormInstanceRecipient', 'FormInstanceRecipient']
---

# FormInstanceRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is a unique identifier | [optional] 
**type** |  **Enum** [  'IDENTITY' ] | Type is a FormInstanceRecipientType value IDENTITY FormInstanceRecipientIdentity | [optional] 
}

## Example

```python
from sailpoint.custom_forms.models.form_instance_recipient import FormInstanceRecipient

form_instance_recipient = FormInstanceRecipient(
id='00000000-0000-0000-0000-000000000000',
type='IDENTITY'
)

```
[[Back to top]](#) 

