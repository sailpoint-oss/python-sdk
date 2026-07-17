---
id: form-instance-created-by
title: FormInstanceCreatedBy
pagination_label: FormInstanceCreatedBy
sidebar_label: FormInstanceCreatedBy
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'FormInstanceCreatedBy', 'FormInstanceCreatedBy'] 
slug: /tools/sdk/python/custom-forms/models/form-instance-created-by
tags: ['SDK', 'Software Development Kit', 'FormInstanceCreatedBy', 'FormInstanceCreatedBy']
---

# FormInstanceCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is a unique identifier | [optional] 
**type** |  **Enum** [  'WORKFLOW_EXECUTION',    'SOURCE' ] | Type is a form instance created by type enum value WORKFLOW_EXECUTION FormInstanceCreatedByTypeWorkflowExecution SOURCE FormInstanceCreatedByTypeSource | [optional] 
}

## Example

```python
from sailpoint.custom_forms.models.form_instance_created_by import FormInstanceCreatedBy

form_instance_created_by = FormInstanceCreatedBy(
id='00000000-0000-0000-0000-000000000000',
type='WORKFLOW_EXECUTION'
)

```
[[Back to top]](#) 

