---
id: v2025-account-updated-single-value-attribute-changes-inner
title: AccountUpdatedSingleValueAttributeChangesInner
pagination_label: AccountUpdatedSingleValueAttributeChangesInner
sidebar_label: AccountUpdatedSingleValueAttributeChangesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountUpdatedSingleValueAttributeChangesInner', 'V2025AccountUpdatedSingleValueAttributeChangesInner'] 
slug: /tools/sdk/python/v2025/models/account-updated-single-value-attribute-changes-inner
tags: ['SDK', 'Software Development Kit', 'AccountUpdatedSingleValueAttributeChangesInner', 'V2025AccountUpdatedSingleValueAttributeChangesInner']
---

# AccountUpdatedSingleValueAttributeChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the attribute that was changed. | [required]
**old_value** | [**AccountUpdatedSingleValueAttributeChangesInnerOldValue**](account-updated-single-value-attribute-changes-inner-old-value) |  | [required]
**new_value** | [**AccountUpdatedSingleValueAttributeChangesInnerNewValue**](account-updated-single-value-attribute-changes-inner-new-value) |  | [required]
}

## Example

```python
from sailpoint.v2025.models.account_updated_single_value_attribute_changes_inner import AccountUpdatedSingleValueAttributeChangesInner

account_updated_single_value_attribute_changes_inner = AccountUpdatedSingleValueAttributeChangesInner(
name='displayName',
old_value=John Doe,
new_value=John A. Doe
)

```
[[Back to top]](#) 

