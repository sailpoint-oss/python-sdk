# LifecycleStateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_name** | **str** | The name of the lifecycle state | 
**manually_updated** | **bool** | Whether the lifecycle state has been manually or automatically set | 

## Example

```python
from sailpoint.v2024.models.lifecycle_state_dto import LifecycleStateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleStateDto from a JSON string
lifecycle_state_dto_instance = LifecycleStateDto.from_json(json)
# print the JSON string representation of the object
print LifecycleStateDto.to_json()

# convert the object into a dict
lifecycle_state_dto_dict = lifecycle_state_dto_instance.to_dict()
# create an instance of LifecycleStateDto from a dict
lifecycle_state_dto_form_dict = lifecycle_state_dto.from_dict(lifecycle_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


