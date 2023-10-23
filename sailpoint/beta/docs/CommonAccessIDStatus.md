# CommonAccessIDStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_ids** | **List[str]** | List of confirmed common access ids. | [optional] 
**denied_ids** | **List[str]** | List of denied common access ids. | [optional] 

## Example

```python
from beta.models.common_access_id_status import CommonAccessIDStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAccessIDStatus from a JSON string
common_access_id_status_instance = CommonAccessIDStatus.from_json(json)
# print the JSON string representation of the object
print CommonAccessIDStatus.to_json()

# convert the object into a dict
common_access_id_status_dict = common_access_id_status_instance.to_dict()
# create an instance of CommonAccessIDStatus from a dict
common_access_id_status_form_dict = common_access_id_status.from_dict(common_access_id_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


