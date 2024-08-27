# BaseSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Segment&#39;s unique ID. | [optional] 
**name** | **str** | Segment&#39;s display name. | [optional] 

## Example

```python
from sailpoint.v3.models.base_segment import BaseSegment

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSegment from a JSON string
base_segment_instance = BaseSegment.from_json(json)
# print the JSON string representation of the object
print(BaseSegment.to_json())

# convert the object into a dict
base_segment_dict = base_segment_instance.to_dict()
# create an instance of BaseSegment from a dict
base_segment_from_dict = BaseSegment.from_dict(base_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


