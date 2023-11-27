# AccessItemAppResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | the access item type. entitlement in this case | [optional] 
**id** | **str** | the access item id | [optional] 
**display_name** | **str** | the access profile display name | [optional] 
**source_name** | **str** | the associated source name if it exists | [optional] 

## Example

```python
from sailpoint.beta.models.access_item_app_response import AccessItemAppResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemAppResponse from a JSON string
access_item_app_response_instance = AccessItemAppResponse.from_json(json)
# print the JSON string representation of the object
print AccessItemAppResponse.to_json()

# convert the object into a dict
access_item_app_response_dict = access_item_app_response_instance.to_dict()
# create an instance of AccessItemAppResponse from a dict
access_item_app_response_form_dict = access_item_app_response.from_dict(access_item_app_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


