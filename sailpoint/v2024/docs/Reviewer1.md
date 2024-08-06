# Reviewer1

Details of the reviewer for certification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The reviewer&#39;s DTO type. | 
**id** | **str** | The reviewer&#39;s ID. | 
**name** | **str** | The reviewer&#39;s display name. | 
**email** | **str** | The reviewing identity&#39;s email. Only applicable to &#x60;IDENTITY&#x60;. | [optional] 

## Example

```python
from sailpoint.v2024.models.reviewer1 import Reviewer1

# TODO update the JSON string below
json = "{}"
# create an instance of Reviewer1 from a JSON string
reviewer1_instance = Reviewer1.from_json(json)
# print the JSON string representation of the object
print Reviewer1.to_json()

# convert the object into a dict
reviewer1_dict = reviewer1_instance.to_dict()
# create an instance of Reviewer1 from a dict
reviewer1_form_dict = reviewer1.from_dict(reviewer1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


