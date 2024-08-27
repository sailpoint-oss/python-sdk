# BrandingItemCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of branding item | 
**product_name** | **str** | product name | 
**action_button_color** | **str** | hex value of color for action button | [optional] 
**active_link_color** | **str** | hex value of color for link | [optional] 
**navigation_color** | **str** | hex value of color for navigation bar | [optional] 
**email_from_address** | **str** | email from address | [optional] 
**login_informational_message** | **str** | login information message | [optional] 
**file_standard** | **bytearray** | png file with logo | [optional] 

## Example

```python
from sailpoint.v3.models.branding_item_create import BrandingItemCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingItemCreate from a JSON string
branding_item_create_instance = BrandingItemCreate.from_json(json)
# print the JSON string representation of the object
print(BrandingItemCreate.to_json())

# convert the object into a dict
branding_item_create_dict = branding_item_create_instance.to_dict()
# create an instance of BrandingItemCreate from a dict
branding_item_create_from_dict = BrandingItemCreate.from_dict(branding_item_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


