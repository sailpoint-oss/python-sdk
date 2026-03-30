---
id: v2026-entitlement-v2-access-model-metadata
title: EntitlementV2AccessModelMetadata
pagination_label: EntitlementV2AccessModelMetadata
sidebar_label: EntitlementV2AccessModelMetadata
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementV2AccessModelMetadata', 'V2026EntitlementV2AccessModelMetadata'] 
slug: /tools/sdk/python/v2026/models/entitlement-v2-access-model-metadata
tags: ['SDK', 'Software Development Kit', 'EntitlementV2AccessModelMetadata', 'V2026EntitlementV2AccessModelMetadata']
---

# EntitlementV2AccessModelMetadata

Additional data to classify the entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[]AccessModelMetadata**](access-model-metadata) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.entitlement_v2_access_model_metadata import EntitlementV2AccessModelMetadata

entitlement_v2_access_model_metadata = EntitlementV2AccessModelMetadata(
attributes=[
                    sailpoint.v2026.models.access_model_metadata.Access Model Metadata(
                        key = 'iscCsp', 
                        name = 'CSP', 
                        multiselect = True, 
                        status = 'active', 
                        type = 'governance', 
                        object_types = [general], 
                        description = 'Indicates the type of deployment environment of an access item.', 
                        values = [
                            sailpoint.v2026.models.access_model_metadata_values_inner.AccessModelMetadata_values_inner(
                                value = 'development', 
                                name = 'Development', 
                                status = 'active', )
                            ], )
                    ]
)

```
[[Back to top]](#) 

