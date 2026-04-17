---
id: identity-proofing-result
title: IdentityProofingResult
pagination_label: IdentityProofingResult
sidebar_label: IdentityProofingResult
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityProofingResult', 'IdentityProofingResult'] 
slug: /tools/sdk/python//models/identity-proofing-result
tags: ['SDK', 'Software Development Kit', 'IdentityProofingResult', 'IdentityProofingResult']
---

# IdentityProofingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**identity_proofing_action_id** | **str** |  | [optional] 
**workflow_session_id** | **str** |  | [optional] 
**profile_id** | **str** |  | [optional] 
**proofing_workflow** | **str** |  | [optional] 
**result** |  **Enum** [  'pending',    'pass',    'fail' ] |  | [optional] 
**proofing_attributes** | **map[string]str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.identity_proofing_result import IdentityProofingResult

identity_proofing_result = IdentityProofingResult(
id='',
identity_proofing_action_id='',
workflow_session_id='',
profile_id='',
proofing_workflow='',
result='pending',
proofing_attributes={result=approve},
created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
)

```
[[Back to top]](#) 

