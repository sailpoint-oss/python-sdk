# SpConfigUrl

Format of resolver URLs for Object Configurations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL for the target object endpoint. | [optional] 
**query** | **object** | Any query parameters that are needed for the URL. | [optional] 

## Example

```python
from sailpoint.beta.models.sp_config_url import SpConfigUrl

# TODO update the JSON string below
json = "{}"
# create an instance of SpConfigUrl from a JSON string
sp_config_url_instance = SpConfigUrl.from_json(json)
# print the JSON string representation of the object
print SpConfigUrl.to_json()

# convert the object into a dict
sp_config_url_dict = sp_config_url_instance.to_dict()
# create an instance of SpConfigUrl from a dict
sp_config_url_form_dict = sp_config_url.from_dict(sp_config_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


