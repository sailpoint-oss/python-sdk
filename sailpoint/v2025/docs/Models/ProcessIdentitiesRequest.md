---
id: v2025-process-identities-request
title: ProcessIdentitiesRequest
pagination_label: ProcessIdentitiesRequest
sidebar_label: ProcessIdentitiesRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProcessIdentitiesRequest', 'V2025ProcessIdentitiesRequest'] 
slug: /tools/sdk/python/v2025/models/process-identities-request
tags: ['SDK', 'Software Development Kit', 'ProcessIdentitiesRequest', 'V2025ProcessIdentitiesRequest']
---

# ProcessIdentitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_ids** | **[]str** | List of up to 250 identity IDs to process. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.process_identities_request import ProcessIdentitiesRequest

process_identities_request = ProcessIdentitiesRequest(
identity_ids=[
                    'ef38f94347e94562b5bb8424a56397d8'
                    ]
)

```
[[Back to top]](#) 

