# SegmentVisibilityCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**Expression**](Expression.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.segment_visibility_criteria import SegmentVisibilityCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentVisibilityCriteria from a JSON string
segment_visibility_criteria_instance = SegmentVisibilityCriteria.from_json(json)
# print the JSON string representation of the object
print(SegmentVisibilityCriteria.to_json())

# convert the object into a dict
segment_visibility_criteria_dict = segment_visibility_criteria_instance.to_dict()
# create an instance of SegmentVisibilityCriteria from a dict
segment_visibility_criteria_from_dict = SegmentVisibilityCriteria.from_dict(segment_visibility_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


