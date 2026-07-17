---
id: multi-policy-request
title: MultiPolicyRequest
pagination_label: MultiPolicyRequest
sidebar_label: MultiPolicyRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MultiPolicyRequest', 'MultiPolicyRequest'] 
slug: /tools/sdk/python/sod-policies/models/multi-policy-request
tags: ['SDK', 'Software Development Kit', 'MultiPolicyRequest', 'MultiPolicyRequest']
---

# MultiPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filtered_policy_list** | **[]str** | Multi-policy report will be run for this list of ids | [optional] 
}

## Example

```python
from sailpoint.sod_policies.models.multi_policy_request import MultiPolicyRequest

multi_policy_request = MultiPolicyRequest(
filtered_policy_list=[
                    '["b868cd40-ffa4-4337-9c07-1a51846cfa94","63a07a7b-39a4-48aa-956d-50c827deba2a"]'
                    ]
)

```
[[Back to top]](#) 

