# Segment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The segment&#39;s ID. | [optional] 
**name** | **str** | The segment&#39;s business name. | [optional] 
**created** | **datetime** | The time when the segment is created. | [optional] 
**modified** | **datetime** | The time when the segment is modified. | [optional] 
**description** | **str** | The segment&#39;s optional description. | [optional] 
**owner** | [**OwnerReferenceSegments**](OwnerReferenceSegments.md) |  | [optional] 
**visibility_criteria** | [**SegmentVisibilityCriteria**](SegmentVisibilityCriteria.md) |  | [optional] 
**active** | **bool** | This boolean indicates whether the segment is currently active. Inactive segments have no effect. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.segment import Segment

# TODO update the JSON string below
json = "{}"
# create an instance of Segment from a JSON string
segment_instance = Segment.from_json(json)
# print the JSON string representation of the object
print Segment.to_json()

# convert the object into a dict
segment_dict = segment_instance.to_dict()
# create an instance of Segment from a dict
segment_form_dict = segment.from_dict(segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


