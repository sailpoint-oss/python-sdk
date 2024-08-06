# AccessItemRequesterDto

Access item requester's identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Access item requester&#39;s DTO type. | [optional] 
**id** | **str** | Access item requester&#39;s identity ID. | [optional] 
**name** | **str** | Access item owner&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.v2024.models.access_item_requester_dto import AccessItemRequesterDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemRequesterDto from a JSON string
access_item_requester_dto_instance = AccessItemRequesterDto.from_json(json)
# print the JSON string representation of the object
print AccessItemRequesterDto.to_json()

# convert the object into a dict
access_item_requester_dto_dict = access_item_requester_dto_instance.to_dict()
# create an instance of AccessItemRequesterDto from a dict
access_item_requester_dto_form_dict = access_item_requester_dto.from_dict(access_item_requester_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


