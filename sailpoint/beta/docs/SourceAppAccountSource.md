# SourceAppAccountSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The source ID | [optional] 
**type** | **str** | The source type, will always be \&quot;SOURCE\&quot; | [optional] 
**name** | **str** | The source name | [optional] 
**use_for_password_management** | **bool** | If the source is used for password management | [optional] [default to False]
**password_policies** | [**List[BaseReferenceDto1]**](BaseReferenceDto1.md) | The password policies for the source | [optional] 

## Example

```python
from sailpoint.beta.models.source_app_account_source import SourceAppAccountSource

# TODO update the JSON string below
json = "{}"
# create an instance of SourceAppAccountSource from a JSON string
source_app_account_source_instance = SourceAppAccountSource.from_json(json)
# print the JSON string representation of the object
print(SourceAppAccountSource.to_json())

# convert the object into a dict
source_app_account_source_dict = source_app_account_source_instance.to_dict()
# create an instance of SourceAppAccountSource from a dict
source_app_account_source_from_dict = SourceAppAccountSource.from_dict(source_app_account_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


