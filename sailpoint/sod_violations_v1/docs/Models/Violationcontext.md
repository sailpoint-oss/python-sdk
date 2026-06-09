---
id: violationcontext
title: Violationcontext
pagination_label: Violationcontext
sidebar_label: Violationcontext
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Violationcontext', 'Violationcontext'] 
slug: /tools/sdk/python/v1/models/violationcontext
tags: ['SDK', 'Software Development Kit', 'Violationcontext', 'Violationcontext']
---

# Violationcontext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**ViolationcontextPolicy**](violationcontext-policy) |  | [optional] 
**conflicting_access_criteria** | [**Exceptionaccesscriteria**](exceptionaccesscriteria) |  | [optional] 
}

## Example

```python
from sailpoint.sod_violations_v1.models.violationcontext import Violationcontext

violationcontext = Violationcontext(
policy=sailpoint.sod_violations_v1.models.violationcontext_policy.violationcontext_policy(
                    type = 'ENTITLEMENT', ),
conflicting_access_criteria=sailpoint.sod_violations_v1.models.exceptionaccesscriteria.exceptionaccesscriteria(
                    left_criteria = sailpoint.sod_violations_v1.models.exceptioncriteria.exceptioncriteria(
                        criteria_list = [{"type":"ENTITLEMENT","id":"2c9180866166b5b0016167c32ef31a66","existing":true},{"type":"ENTITLEMENT","id":"2c9180866166b5b0016167c32ef31a67","existing":false}], ), 
                    right_criteria = sailpoint.sod_violations_v1.models.exceptioncriteria.exceptioncriteria(
                        criteria_list = [{"type":"ENTITLEMENT","id":"2c9180866166b5b0016167c32ef31a66","existing":true},{"type":"ENTITLEMENT","id":"2c9180866166b5b0016167c32ef31a67","existing":false}], ), )
)

```
[[Back to top]](#) 

