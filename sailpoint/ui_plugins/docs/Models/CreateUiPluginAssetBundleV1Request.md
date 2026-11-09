---
id: create-ui-plugin-asset-bundle-v1-request
title: CreateUiPluginAssetBundleV1Request
pagination_label: CreateUiPluginAssetBundleV1Request
sidebar_label: CreateUiPluginAssetBundleV1Request
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateUiPluginAssetBundleV1Request', 'CreateUiPluginAssetBundleV1Request'] 
slug: /tools/sdk/python/ui-plugins/models/create-ui-plugin-asset-bundle-v1-request
tags: ['SDK', 'Software Development Kit', 'CreateUiPluginAssetBundleV1Request', 'CreateUiPluginAssetBundleV1Request']
---

# CreateUiPluginAssetBundleV1Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **[]bytearray** | Repeatable form field. Send one part per file; use the part filename for the bundle-relative path (e.g. `assets/app.js`). | [required]
}

## Example

```python
from sailpoint.ui_plugins.models.create_ui_plugin_asset_bundle_v1_request import CreateUiPluginAssetBundleV1Request

create_ui_plugin_asset_bundle_v1_request = CreateUiPluginAssetBundleV1Request(
file=[
                    bytes(b'blah')
                    ]
)

```
[[Back to top]](#) 

