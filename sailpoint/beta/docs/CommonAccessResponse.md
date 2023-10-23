# CommonAccessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**CommonAccessItemAccess**](CommonAccessItemAccess.md) |  | [optional] 
**status** | **str** | CONFIRMED or DENIED | [optional] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**reviewed_by_user** | **bool** | true if user has confirmed or denied status | [optional] 
**last_reviewed** | **datetime** |  | [optional] [readonly] 

## Example

```python
from beta.models.common_access_response import CommonAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAccessResponse from a JSON string
common_access_response_instance = CommonAccessResponse.from_json(json)
# print the JSON string representation of the object
print CommonAccessResponse.to_json()

# convert the object into a dict
common_access_response_dict = common_access_response_instance.to_dict()
# create an instance of CommonAccessResponse from a dict
common_access_response_form_dict = common_access_response.from_dict(common_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


