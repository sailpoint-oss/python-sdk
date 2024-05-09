# TenantUiMetadataItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iframe_white_list** | **str** | Parameter that organizational administrators can adjust to permit another domain to encapsulate IDN within an iframe. If you would like to reset the value use \&quot;null\&quot;. It will only allow include into iframe non authenticated portions of the product, such as password reset. | [optional] 
**username_label** | **str** | Descriptor for the username input field. If you would like to reset the value use \&quot;null\&quot;. | [optional] 
**username_empty_text** | **str** | Placeholder text displayed in the username input field. If you would like to reset the value use \&quot;null\&quot;. | [optional] 

## Example

```python
from sailpoint.beta.models.tenant_ui_metadata_item_response import TenantUiMetadataItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUiMetadataItemResponse from a JSON string
tenant_ui_metadata_item_response_instance = TenantUiMetadataItemResponse.from_json(json)
# print the JSON string representation of the object
print TenantUiMetadataItemResponse.to_json()

# convert the object into a dict
tenant_ui_metadata_item_response_dict = tenant_ui_metadata_item_response_instance.to_dict()
# create an instance of TenantUiMetadataItemResponse from a dict
tenant_ui_metadata_item_response_form_dict = tenant_ui_metadata_item_response.from_dict(tenant_ui_metadata_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


