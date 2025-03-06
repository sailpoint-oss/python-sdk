# OutlierValueType

The data type of the value field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The data type of the value field | [optional] 
**ordinal** | **int** | The position of the value type | [optional] 

## Example

```python
from sailpoint.v2024.models.outlier_value_type import OutlierValueType

# TODO update the JSON string below
json = "{}"
# create an instance of OutlierValueType from a JSON string
outlier_value_type_instance = OutlierValueType.from_json(json)
# print the JSON string representation of the object
print(OutlierValueType.to_json())

# convert the object into a dict
outlier_value_type_dict = outlier_value_type_instance.to_dict()
# create an instance of OutlierValueType from a dict
outlier_value_type_from_dict = OutlierValueType.from_dict(outlier_value_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


