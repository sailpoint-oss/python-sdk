# TenantUiMetadataItemUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iframe_white_list** | **str** | Parameter that organizational administrators can adjust to permit another domain to encapsulate IDN within an iframe. If you would like to reset the value use \&quot;null\&quot;. It will only allow include into iframe non authenticated portions of the product, such as password reset. | [optional] 
**username_label** | **str** | Descriptor for the username input field. If you would like to reset the value use \&quot;null\&quot;. | [optional] 
**username_empty_text** | **str** | Placeholder text displayed in the username input field. If you would like to reset the value use \&quot;null\&quot;. | [optional] 

## Example

```python
from sailpoint.beta.models.tenant_ui_metadata_item_update_request import TenantUiMetadataItemUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUiMetadataItemUpdateRequest from a JSON string
tenant_ui_metadata_item_update_request_instance = TenantUiMetadataItemUpdateRequest.from_json(json)
# print the JSON string representation of the object
print TenantUiMetadataItemUpdateRequest.to_json()

# convert the object into a dict
tenant_ui_metadata_item_update_request_dict = tenant_ui_metadata_item_update_request_instance.to_dict()
# create an instance of TenantUiMetadataItemUpdateRequest from a dict
tenant_ui_metadata_item_update_request_form_dict = tenant_ui_metadata_item_update_request.from_dict(tenant_ui_metadata_item_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


