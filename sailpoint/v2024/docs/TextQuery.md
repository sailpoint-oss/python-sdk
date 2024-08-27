# TextQuery

Query parameters used to construct an Elasticsearch text query object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms** | **List[str]** | Words or characters that specify a particular thing to be searched for. | 
**fields** | **List[str]** | The fields to be searched. | 
**match_any** | **bool** | Indicates that at least one of the terms must be found in the specified fields;  otherwise, all terms must be found. | [optional] [default to False]
**contains** | **bool** | Indicates that the terms can be located anywhere in the specified fields;  otherwise, the fields must begin with the terms. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.text_query import TextQuery

# TODO update the JSON string below
json = "{}"
# create an instance of TextQuery from a JSON string
text_query_instance = TextQuery.from_json(json)
# print the JSON string representation of the object
print(TextQuery.to_json())

# convert the object into a dict
text_query_dict = text_query_instance.to_dict()
# create an instance of TextQuery from a dict
text_query_from_dict = TextQuery.from_dict(text_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


