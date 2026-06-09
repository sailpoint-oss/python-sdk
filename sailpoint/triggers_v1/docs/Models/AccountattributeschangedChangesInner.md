---
id: accountattributeschanged-changes-inner
title: AccountattributeschangedChangesInner
pagination_label: AccountattributeschangedChangesInner
sidebar_label: AccountattributeschangedChangesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountattributeschangedChangesInner', 'AccountattributeschangedChangesInner'] 
slug: /tools/sdk/python/v1/models/accountattributeschanged-changes-inner
tags: ['SDK', 'Software Development Kit', 'AccountattributeschangedChangesInner', 'AccountattributeschangedChangesInner']
---

# AccountattributeschangedChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The name of the attribute. | [required]
**old_value** | [**AccountattributeschangedChangesInnerOldValue**](accountattributeschanged-changes-inner-old-value) |  | [required]
**new_value** | [**AccountattributeschangedChangesInnerNewValue**](accountattributeschanged-changes-inner-new-value) |  | [required]
}

## Example

```python
from sailpoint.triggers_v1.models.accountattributeschanged_changes_inner import AccountattributeschangedChangesInner

accountattributeschanged_changes_inner = AccountattributeschangedChangesInner(
attribute='sn',
old_value=doe,
new_value=ryans
)

```
[[Back to top]](#) 

