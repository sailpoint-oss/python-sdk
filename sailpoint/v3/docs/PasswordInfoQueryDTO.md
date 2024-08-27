# PasswordInfoQueryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | The login name of the user | [optional] 
**source_name** | **str** | The display name of the source | [optional] 

## Example

```python
from sailpoint.v3.models.password_info_query_dto import PasswordInfoQueryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordInfoQueryDTO from a JSON string
password_info_query_dto_instance = PasswordInfoQueryDTO.from_json(json)
# print the JSON string representation of the object
print(PasswordInfoQueryDTO.to_json())

# convert the object into a dict
password_info_query_dto_dict = password_info_query_dto_instance.to_dict()
# create an instance of PasswordInfoQueryDTO from a dict
password_info_query_dto_from_dict = PasswordInfoQueryDTO.from_dict(password_info_query_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


