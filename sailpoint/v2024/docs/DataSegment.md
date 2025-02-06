# DataSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The segment&#39;s ID. | [optional] 
**name** | **str** | The segment&#39;s business name. | [optional] 
**created** | **datetime** | The time when the segment is created. | [optional] 
**modified** | **datetime** | The time when the segment is modified. | [optional] 
**description** | **str** | The segment&#39;s optional description. | [optional] 
**scopes** | [**List[Scope]**](Scope.md) | List of Scopes that are assigned to the segment | [optional] 
**member_selection** | [**List[Ref]**](Ref.md) | List of Identities that are assigned to the segment | [optional] 
**member_filter** | [**VisibilityCriteria**](VisibilityCriteria.md) |  | [optional] 
**membership** | [**MembershipType**](MembershipType.md) |  | [optional] 
**enabled** | **bool** | This boolean indicates whether the segment is currently active. Inactive segments have no effect. | [optional] [default to False]
**published** | **bool** | This boolean indicates whether the segment is being applied to the accounts. If unpublished its being actively modified to until published | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.data_segment import DataSegment

# TODO update the JSON string below
json = "{}"
# create an instance of DataSegment from a JSON string
data_segment_instance = DataSegment.from_json(json)
# print the JSON string representation of the object
print(DataSegment.to_json())

# convert the object into a dict
data_segment_dict = data_segment_instance.to_dict()
# create an instance of DataSegment from a dict
data_segment_from_dict = DataSegment.from_dict(data_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


