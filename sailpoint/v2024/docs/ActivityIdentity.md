# ActivityIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**type** | **str** | Type of object | [optional] 

## Example

```python
from sailpoint.v2024.models.activity_identity import ActivityIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityIdentity from a JSON string
activity_identity_instance = ActivityIdentity.from_json(json)
# print the JSON string representation of the object
print(ActivityIdentity.to_json())

# convert the object into a dict
activity_identity_dict = activity_identity_instance.to_dict()
# create an instance of ActivityIdentity from a dict
activity_identity_from_dict = ActivityIdentity.from_dict(activity_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


