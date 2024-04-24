from sailpoint.v3.api.search_api import SearchApi
from sailpoint.v3.models.search import Search
from typing import TypeVar

T = TypeVar('T')

class PaginationParams:
    limit: int
    offset: int
    count: bool
    filters: str
    sorters: str
    increment: int

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)

class Paginator:

    @staticmethod
    def paginate(T, result_limit, **kwargs) -> T:
        
        # If the total result limit is not provided, set a default of 1000 records to fetch.
        result_limit = result_limit if result_limit else 1000
        increment = kwargs.get('limit') if kwargs.get('limit') is not None else 250
        kwargs['offset'] = kwargs.get('offset') if kwargs.get('offset') is not None else 0

        modified = []
        while True:
            print(f'Paginating call, offset = {kwargs["offset"]}')

            # Call endpoint and pass any arguments
            results = T(**kwargs)

            if isinstance(results, list):
                modified = modified + results
                if len(results) < increment or (len(modified) >= result_limit and result_limit > 0):
                # Return results, we have either received less results than the limit 
                # passed to the api or we've reached the limit specified by the user
                    return modified
            else:
                modified = modified + results.data
                if len(results.data) < increment or (len(modified) >= result_limit and result_limit > 0):
                    # Return results, we have either received less results than the limit 
                    # passed to the api or we've reached the limit specified by the user
                    results.data = modified
                    return results
                            
            kwargs['offset'] += increment

    @staticmethod
    def paginate_search(search_api: SearchApi, search: Search, increment: int, limit: int):
        increment = increment if increment else 250
        offset = 0
        max_limit = limit if limit else 0

        modified = []

        if search.sort is None or len(search.sort) != 1:
            raise Exception('search query must include exactly one sort parameter to paginate properly')
        
        while True:
            print(f'Paginating call, offset = {offset}')
            results = search_api.search_post(search, None, increment)
            modified = modified + results
            
            print(f'Received {len(results)} results')

            if len(results) < increment or (len(modified) >= max_limit and max_limit > 0):
                results = modified
                return results
            else:
                result = results[len(results) - 1]
                if result[search.sort[0].strip('+-')] is not None:
                    next_search_after = result[str(search.sort[0]).strip('+-')]
                    search.search_after = [next_search_after]
                else:
                    raise Exception('Search unexpectedly did not return a result we can search after!')

            offset += increment

    @staticmethod
    def paginate_search_with_http_info(search_api: SearchApi, search: Search, increment: int, limit: int):
        increment = increment if increment else 250
        offset = 0
        max_limit = limit if limit else 0

        modified = []

        if search.sort is None or len(search.sort) != 1:
            raise Exception('search query must include exactly one sort parameter to paginate properly')
        
        while True:
            print(f'Paginating call, offset = {offset}')
            results = search_api.search_post_with_http_info(search, None, increment)
            modified = modified + results.data
            
            print(f'Recieved {len(results.data)} results')

            if len(results.data) < increment or (len(modified) >= max_limit and max_limit > 0):
                results.data = modified
                return results
            else:
                result = results.data[len(results.data) - 1]
                if result[search.sort[0].strip('+-')] is not None:
                    next_search_after = result[str(search.sort[0]).strip('+-')]
                    search.search_after = [next_search_after]
                else:
                    raise Exception('Search unexpectedly did not return a result we can search after!')

            offset += increment