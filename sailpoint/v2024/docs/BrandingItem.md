# BrandingItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of branding item | [optional] 
**product_name** | **str** | product name | [optional] 
**action_button_color** | **str** | hex value of color for action button | [optional] 
**active_link_color** | **str** | hex value of color for link | [optional] 
**navigation_color** | **str** | hex value of color for navigation bar | [optional] 
**email_from_address** | **str** | email from address | [optional] 
**standard_logo_url** | **str** | url to standard logo | [optional] 
**login_informational_message** | **str** | login information message | [optional] 

## Example

```python
from sailpoint.v2024.models.branding_item import BrandingItem

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingItem from a JSON string
branding_item_instance = BrandingItem.from_json(json)
# print the JSON string representation of the object
print BrandingItem.to_json()

# convert the object into a dict
branding_item_dict = branding_item_instance.to_dict()
# create an instance of BrandingItem from a dict
branding_item_form_dict = branding_item.from_dict(branding_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


