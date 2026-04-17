---
id: batch-workflow-options
title: BatchWorkflowOptions
pagination_label: BatchWorkflowOptions
sidebar_label: BatchWorkflowOptions
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BatchWorkflowOptions', 'BatchWorkflowOptions'] 
slug: /tools/sdk/python//models/batch-workflow-options
tags: ['SDK', 'Software Development Kit', 'BatchWorkflowOptions', 'BatchWorkflowOptions']
---

# BatchWorkflowOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_profiles** |  **Enum** [  'true',    'false' ] | Used for batch workflows. | [optional] 
**multiple_requests** |  **Enum** [  'true',    'false' ] | Used for batch workflows for if multiple requests. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.batch_workflow_options import BatchWorkflowOptions

batch_workflow_options = BatchWorkflowOptions(
all_profiles='true',
multiple_requests='false'
)

```
[[Back to top]](#) 

