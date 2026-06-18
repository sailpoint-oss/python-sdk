---
id: v2026-source-dataset-resource
title: SourceDatasetResource
pagination_label: SourceDatasetResource
sidebar_label: SourceDatasetResource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceDatasetResource', 'V2026SourceDatasetResource'] 
slug: /tools/sdk/python/v2026/models/source-dataset-resource
tags: ['SDK', 'Software Development Kit', 'SourceDatasetResource', 'V2026SourceDatasetResource']
---

# SourceDatasetResource

Resource definition for a source. The resource is reconstructed from source schema data (resourceId/resourceType in schema config and schema objectType as name).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource identifier from source schema config. | [optional] 
**name** | **str** | Display name of the resource. | [optional] 
**features** | **[]str** | Feature identifiers supported by this resource. | [optional] 
**type** | **str** | Resource type from source schema config. | [optional] 
**var_schema** | [**ModelSchema**](model-schema) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.source_dataset_resource import SourceDatasetResource

source_dataset_resource = SourceDatasetResource(
id='aws:iam-role',
name='Account',
features=[Create, Delete],
type='std:resource',
var_schema=sailpoint.v2026.models.schema.Schema(
                    id = '2c9180835d191a86015d28455b4a2329', 
                    name = 'account', 
                    native_object_type = 'User', 
                    identity_attribute = 'sAMAccountName', 
                    display_attribute = 'distinguishedName', 
                    hierarchy_attribute = 'memberOf', 
                    include_permissions = False, 
                    features = [PROVISIONING, NO_PERMISSIONS_PROVISIONING, GROUPS_HAVE_MEMBERS], 
                    configuration = {groupMemberAttribute=member}, 
                    attributes = [{name=sAMAccountName, type=STRING, isMultiValued=false, isEntitlement=false, isGroup=false}, {name=memberOf, type=STRING, schema={type=CONNECTOR_SCHEMA, id=2c9180887671ff8c01767b4671fc7d60, name=group}, description=Group membership, isMultiValued=true, isEntitlement=true, isGroup=true}], 
                    created = '2019-12-24T22:32:58.104Z', 
                    modified = '2019-12-31T20:22:28.104Z', )
)

```
[[Back to top]](#) 

