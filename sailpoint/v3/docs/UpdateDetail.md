# UpdateDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The detailed message for an update. Typically the relevent error message when status is error. | [optional] 
**script_name** | **str** | The connector script name | [optional] 
**updated_files** | **List[str]** | The list of updated files supported by the connector | [optional] 
**status** | **str** | The connector update status | [optional] 

## Example

```python
from sailpoint.v3.models.update_detail import UpdateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDetail from a JSON string
update_detail_instance = UpdateDetail.from_json(json)
# print the JSON string representation of the object
print(UpdateDetail.to_json())

# convert the object into a dict
update_detail_dict = update_detail_instance.to_dict()
# create an instance of UpdateDetail from a dict
update_detail_from_dict = UpdateDetail.from_dict(update_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


