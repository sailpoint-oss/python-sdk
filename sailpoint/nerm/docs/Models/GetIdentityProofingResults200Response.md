---
id: get-identity-proofing-results200-response
title: GetIdentityProofingResults200Response
pagination_label: GetIdentityProofingResults200Response
sidebar_label: GetIdentityProofingResults200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetIdentityProofingResults200Response', 'GetIdentityProofingResults200Response'] 
slug: /tools/sdk/python//models/get-identity-proofing-results200-response
tags: ['SDK', 'Software Development Kit', 'GetIdentityProofingResults200Response', 'GetIdentityProofingResults200Response']
---

# GetIdentityProofingResults200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_proofing_results** | [**[]IdentityProofingResult**](identity-proofing-result) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_identity_proofing_results200_response import GetIdentityProofingResults200Response

get_identity_proofing_results200_response = GetIdentityProofingResults200Response(
identity_proofing_results=[
                    sailpoint.nerm.models.identity_proofing_result.IdentityProofingResult(
                        id = '', 
                        identity_proofing_action_id = '', 
                        workflow_session_id = '', 
                        profile_id = '', 
                        proofing_workflow = '', 
                        result = 'pending', 
                        proofing_attributes = {result=approve}, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
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

