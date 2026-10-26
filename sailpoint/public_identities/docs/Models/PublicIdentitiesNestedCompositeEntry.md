---
id: public-identities-nested-composite-entry
title: PublicIdentitiesNestedCompositeEntry
pagination_label: PublicIdentitiesNestedCompositeEntry
sidebar_label: PublicIdentitiesNestedCompositeEntry
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PublicIdentitiesNestedCompositeEntry', 'PublicIdentitiesNestedCompositeEntry'] 
slug: /tools/sdk/python/public-identities/models/public-identities-nested-composite-entry
tags: ['SDK', 'Software Development Kit', 'PublicIdentitiesNestedCompositeEntry', 'PublicIdentitiesNestedCompositeEntry']
---

# PublicIdentitiesNestedCompositeEntry

A COMPOSITE query entry that nests another querySet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_type** |  **Enum** [  'COMPOSITE' ] | Entry type discriminator. Must be COMPOSITE for nested query sets. | [required]
**query_set** | [**PublicIdentitiesNestedQuerySet**](public-identities-nested-query-set) | Nested query set for this COMPOSITE entry. | [required]
}

## Example

```python
from sailpoint.public_identities.models.public_identities_nested_composite_entry import PublicIdentitiesNestedCompositeEntry

public_identities_nested_composite_entry = PublicIdentitiesNestedCompositeEntry(
query_type='COMPOSITE',
query_set=sailpoint.public_identities.models.public_identities_nested_query_set.Public Identities Nested Query Set(
                    match_any = True, 
                    entries = [
                        sailpoint.public_identities.models.public_identities_text_entry.Public Identities Text Entry(
                            query_type = 'TEXT', 
                            text_query = null, )
                        ], )
)

```
[[Back to top]](#) 

