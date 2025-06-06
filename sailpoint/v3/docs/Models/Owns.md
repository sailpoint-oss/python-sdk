---
id: owns
title: Owns
pagination_label: Owns
sidebar_label: Owns
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Owns', 'Owns'] 
slug: /tools/sdk/python/v3/models/owns
tags: ['SDK', 'Software Development Kit', 'Owns', 'Owns']
---

# Owns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**[]Reference**](reference) |  | [optional] 
**entitlements** | [**[]Reference**](reference) |  | [optional] 
**access_profiles** | [**[]Reference**](reference) |  | [optional] 
**roles** | [**[]Reference**](reference) |  | [optional] 
**apps** | [**[]Reference**](reference) |  | [optional] 
**governance_groups** | [**[]Reference**](reference) |  | [optional] 
**fallback_approver** | **bool** |  | [optional] 
}

## Example

```python
from sailpoint.v3.models.owns import Owns

owns = Owns(
sources=[
                    sailpoint.v3.models.reference.Reference(
                        id = '2c91808568c529c60168cca6f90c1313', 
                        name = 'John Doe', )
                    ],
entitlements=[
                    sailpoint.v3.models.reference.Reference(
                        id = '2c91808568c529c60168cca6f90c1313', 
                        name = 'John Doe', )
                    ],
access_profiles=[
                    sailpoint.v3.models.reference.Reference(
                        id = '2c91808568c529c60168cca6f90c1313', 
                        name = 'John Doe', )
                    ],
roles=[
                    sailpoint.v3.models.reference.Reference(
                        id = '2c91808568c529c60168cca6f90c1313', 
                        name = 'John Doe', )
                    ],
apps=[
                    sailpoint.v3.models.reference.Reference(
                        id = '2c91808568c529c60168cca6f90c1313', 
                        name = 'John Doe', )
                    ],
governance_groups=[
                    sailpoint.v3.models.reference.Reference(
                        id = '2c91808568c529c60168cca6f90c1313', 
                        name = 'John Doe', )
                    ],
fallback_approver=False
)

```
[[Back to top]](#) 

