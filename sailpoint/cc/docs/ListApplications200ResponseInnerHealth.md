# ListApplications200ResponseInnerHealth


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**last_changed** | **str** |  | [optional] 
**since** | **float** |  | [optional] 
**healthy** | **bool** |  | [optional] 

## Example

```python
from sailpoint.cc.models.list_applications200_response_inner_health import ListApplications200ResponseInnerHealth

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplications200ResponseInnerHealth from a JSON string
list_applications200_response_inner_health_instance = ListApplications200ResponseInnerHealth.from_json(json)
# print the JSON string representation of the object
print ListApplications200ResponseInnerHealth.to_json()

# convert the object into a dict
list_applications200_response_inner_health_dict = list_applications200_response_inner_health_instance.to_dict()
# create an instance of ListApplications200ResponseInnerHealth from a dict
list_applications200_response_inner_health_form_dict = list_applications200_response_inner_health.from_dict(list_applications200_response_inner_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


