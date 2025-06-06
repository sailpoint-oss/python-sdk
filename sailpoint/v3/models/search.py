# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
import warnings

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sailpoint.v3.models.aggregation_type import AggregationType
from sailpoint.v3.models.filter import Filter
from sailpoint.v3.models.index import Index
from sailpoint.v3.models.query import Query
from sailpoint.v3.models.query_result_filter import QueryResultFilter
from sailpoint.v3.models.query_type import QueryType
from sailpoint.v3.models.search_aggregation_specification import SearchAggregationSpecification
from sailpoint.v3.models.text_query import TextQuery
from sailpoint.v3.models.type_ahead_query import TypeAheadQuery
from typing import Optional, Set
from typing_extensions import Self

class Search(BaseModel):
    """
    Search
    """ # noqa: E501
    indices: Optional[List[Index]] = Field(default=None, description="The names of the Elasticsearch indices in which to search. If none are provided, then all indices will be searched.")
    query_type: Optional[QueryType] = Field(default=QueryType.SAILPOINT, alias="queryType")
    query_version: Optional[Any] = Field(default=None, alias="queryVersion")
    query: Optional[Query] = None
    query_dsl: Optional[Dict[str, Any]] = Field(default=None, description="The search query using the Elasticsearch [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/7.10/query-dsl.html) syntax.", alias="queryDsl")
    text_query: Optional[TextQuery] = Field(default=None, alias="textQuery")
    type_ahead_query: Optional[TypeAheadQuery] = Field(default=None, alias="typeAheadQuery")
    include_nested: Optional[StrictBool] = Field(default=True, description="Indicates whether nested objects from returned search results should be included.", alias="includeNested")
    query_result_filter: Optional[QueryResultFilter] = Field(default=None, alias="queryResultFilter")
    aggregation_type: Optional[AggregationType] = Field(default=AggregationType.DSL, alias="aggregationType")
    aggregations_version: Optional[Any] = Field(default=None, alias="aggregationsVersion")
    aggregations_dsl: Optional[Dict[str, Any]] = Field(default=None, description="The aggregation search query using Elasticsearch [Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/5.2/search-aggregations.html) syntax.", alias="aggregationsDsl")
    aggregations: Optional[SearchAggregationSpecification] = None
    sort: Optional[List[StrictStr]] = Field(default=None, description="The fields to be used to sort the search results. Use + or - to specify the sort direction.")
    search_after: Optional[List[StrictStr]] = Field(default=None, description="Used to begin the search window at the values specified. This parameter consists of the last values of the sorted fields in the current record set. This is used to expand the Elasticsearch limit of 10K records by shifting the 10K window to begin at this value. It is recommended that you always include the ID of the object in addition to any other fields on this parameter in order to ensure you don't get duplicate results while paging. For example, when searching for identities, if you are sorting by displayName you will also want to include ID, for example [\"displayName\", \"id\"].  If the last identity ID in the search result is 2c91808375d8e80a0175e1f88a575221 and the last displayName is \"John Doe\", then using that displayName and ID will start a new search after this identity. The searchAfter value will look like [\"John Doe\",\"2c91808375d8e80a0175e1f88a575221\"]", alias="searchAfter")
    filters: Optional[Dict[str, Filter]] = Field(default=None, description="The filters to be applied for each filtered field name.")
    __properties: ClassVar[List[str]] = ["indices", "queryType", "queryVersion", "query", "queryDsl", "textQuery", "typeAheadQuery", "includeNested", "queryResultFilter", "aggregationType", "aggregationsVersion", "aggregationsDsl", "aggregations", "sort", "searchAfter", "filters"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Search from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of query
        if self.query:
            _dict['query'] = self.query.to_dict()
        # override the default output from pydantic by calling `to_dict()` of text_query
        if self.text_query:
            _dict['textQuery'] = self.text_query.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type_ahead_query
        if self.type_ahead_query:
            _dict['typeAheadQuery'] = self.type_ahead_query.to_dict()
        # override the default output from pydantic by calling `to_dict()` of query_result_filter
        if self.query_result_filter:
            _dict['queryResultFilter'] = self.query_result_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aggregations
        if self.aggregations:
            _dict['aggregations'] = self.aggregations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in filters (dict)
        _field_dict = {}
        if self.filters:
            for _key_filters in self.filters:
                if self.filters[_key_filters]:
                    _field_dict[_key_filters] = self.filters[_key_filters].to_dict()
            _dict['filters'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Search from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "indices": obj.get("indices"),
            "queryType": obj.get("queryType") if obj.get("queryType") is not None else QueryType.SAILPOINT,
            "queryVersion": obj.get("queryVersion"),
            "query": Query.from_dict(obj["query"]) if obj.get("query") is not None else None,
            "queryDsl": obj.get("queryDsl"),
            "textQuery": TextQuery.from_dict(obj["textQuery"]) if obj.get("textQuery") is not None else None,
            "typeAheadQuery": TypeAheadQuery.from_dict(obj["typeAheadQuery"]) if obj.get("typeAheadQuery") is not None else None,
            "includeNested": obj.get("includeNested") if obj.get("includeNested") is not None else True,
            "queryResultFilter": QueryResultFilter.from_dict(obj["queryResultFilter"]) if obj.get("queryResultFilter") is not None else None,
            "aggregationType": obj.get("aggregationType") if obj.get("aggregationType") is not None else AggregationType.DSL,
            "aggregationsVersion": obj.get("aggregationsVersion"),
            "aggregationsDsl": obj.get("aggregationsDsl"),
            "aggregations": SearchAggregationSpecification.from_dict(obj["aggregations"]) if obj.get("aggregations") is not None else None,
            "sort": obj.get("sort"),
            "searchAfter": obj.get("searchAfter"),
            "filters": dict(
                (_k, Filter.from_dict(_v))
                for _k, _v in obj["filters"].items()
            )
            if obj.get("filters") is not None
            else None
        })
        return _obj


