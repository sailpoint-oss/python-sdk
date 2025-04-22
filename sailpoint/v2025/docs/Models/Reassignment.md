---
id: v2025-reassignment
title: Reassignment
pagination_label: Reassignment
sidebar_label: Reassignment
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Reassignment', 'V2025Reassignment'] 
slug: /tools/sdk/python/v2025/models/reassignment
tags: ['SDK', 'Software Development Kit', 'Reassignment', 'V2025Reassignment']
---

# Reassignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**CertificationReference**](certification-reference) |  | [optional] 
**comment** | **str** | The comment entered when the Certification was reassigned | [optional] 
}

## Example

```python
from sailpoint.v2025.models.reassignment import Reassignment

reassignment = Reassignment(
var_from=sailpoint.v2025.models.certification_reference.CertificationReference(
                    id = 'ef38f94347e94562b5bb8424a56397d8', 
                    name = 'Certification Name', 
                    type = 'CERTIFICATION', 
                    reviewer = sailpoint.v2025.models.reviewer.Reviewer(
                        id = 'ef38f94347e94562b5bb8424a56397d8', 
                        name = 'Reviewer Name', 
                        email = 'reviewer@test.com', 
                        type = 'IDENTITY', 
                        created = '2018-06-25T20:22:28.104Z', 
                        modified = '2018-06-25T20:22:28.104Z', ), ),
comment='Reassigned for a reason'
)

```
[[Back to top]](#) 

