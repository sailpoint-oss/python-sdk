# MessageCatalogDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | The language in which the messages are returned | [optional] 
**messages** | [**List[ResourceBundleMessage]**](ResourceBundleMessage.md) | The list of message with their keys and formats | [optional] 

## Example

```python
from beta.models.message_catalog_dto import MessageCatalogDto

# TODO update the JSON string below
json = "{}"
# create an instance of MessageCatalogDto from a JSON string
message_catalog_dto_instance = MessageCatalogDto.from_json(json)
# print the JSON string representation of the object
print MessageCatalogDto.to_json()

# convert the object into a dict
message_catalog_dto_dict = message_catalog_dto_instance.to_dict()
# create an instance of MessageCatalogDto from a dict
message_catalog_dto_form_dict = message_catalog_dto.from_dict(message_catalog_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


