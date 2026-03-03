from sailpoint.v3.api.search_api import SearchApi
from sailpoint.v3.models.search import Search
from typing import Any, Iterator, Optional, Tuple, Type, TypeVar

T = TypeVar('T')
TItem = TypeVar('TItem')

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
    def paginate_stream(
        api_call,
        result_limit: Optional[int] = None,
        *,
        model: Optional[Type[TItem]] = None,
        **kwargs
    ) -> Iterator[TItem]:
        """
        Stream paginated results by yielding items as each API page is received.
        Optional model parameter is for typing only (e.g. Iterator[Account] when model=Account).
        """
        result_limit = result_limit if result_limit else 1000
        increment = kwargs.get('limit') if kwargs.get('limit') is not None else 250
        kwargs['offset'] = kwargs.get('offset') if kwargs.get('offset') is not None else 0
        yielded = 0

        while True:
            print(f'Paginating call, offset = {kwargs["offset"]}')

            results = api_call(**kwargs)

            if isinstance(results, list):
                batch = results
            else:
                batch = results.data

            for item in batch:
                yield item
                yielded += 1
                if result_limit > 0 and yielded >= result_limit:
                    return

            if len(batch) < increment:
                return

            kwargs['offset'] += increment

    @staticmethod
    def paginate_stream_with_http_info(
        api_call,
        result_limit: Optional[int] = None,
        *,
        model: Optional[Type[TItem]] = None,
        **kwargs
    ) -> Tuple[Any, Iterator[TItem]]:
        """
        Stream paginated results from a _with_http_info API call.
        Expects api_call to return an object with .data (and typically .status_code).
        Returns (first_response, iterator) so the caller can check status_code/headers
        and then iterate over items.
        """
        result_limit = result_limit if result_limit else 1000
        increment = kwargs.get('limit') if kwargs.get('limit') is not None else 250
        kwargs['offset'] = kwargs.get('offset') if kwargs.get('offset') is not None else 0

        print(f'Paginating call, offset = {kwargs["offset"]}')
        results = api_call(**kwargs)
        first_response = results
        batch = results.data
        yielded = 0

        def _stream():
            nonlocal yielded, batch
            for item in batch:
                yield item
                yielded += 1
                if result_limit > 0 and yielded >= result_limit:
                    return

            if len(batch) < increment:
                return

            while True:
                kwargs['offset'] += increment
                print(f'Paginating call, offset = {kwargs["offset"]}')
                batch = api_call(**kwargs).data

                for item in batch:
                    yield item
                    yielded += 1
                    if result_limit > 0 and yielded >= result_limit:
                        return

                if len(batch) < increment:
                    return

        return (first_response, _stream())

    @staticmethod
    def paginate_stream_search(search_api: SearchApi, search: Search, increment: int, limit: int):
        """
        Stream search results by yielding each result as it is received from each API page.
        """
        increment = increment if increment else 250
        max_limit = limit if limit else 0
        yielded = 0

        if search.sort is None or len(search.sort) != 1:
            raise Exception('search query must include exactly one sort parameter to paginate properly')

        while True:
            print(f'Paginating call')
            results = search_api.search_post(search, None, increment)

            for result in results:
                yield result
                yielded += 1
                if max_limit > 0 and yielded >= max_limit:
                    return

            print(f'Received {len(results)} results')

            if len(results) < increment:
                return

            result = results[len(results) - 1]
            if result[search.sort[0].strip('+-')] is not None:
                next_search_after = result[str(search.sort[0]).strip('+-')]
                search.search_after = [next_search_after]
            else:
                raise Exception('Search unexpectedly did not return a result we can search after!')

    @staticmethod
    def paginate_stream_search_with_http_info(
        search_api: SearchApi, search: Search, increment: int, limit: int
    ) -> Tuple[Any, Iterator[Any]]:
        """
        Stream search results from search_post_with_http_info.
        Returns (first_response, iterator) so the caller can check status_code/headers
        and then iterate over items.
        """
        increment = increment if increment else 250
        max_limit = limit if limit else 0
        yielded = 0

        if search.sort is None or len(search.sort) != 1:
            raise Exception('search query must include exactly one sort parameter to paginate properly')

        print(f'Paginating call')
        results = search_api.search_post_with_http_info(search, None, increment)
        first_response = results
        batch = results.data

        def _stream():
            nonlocal yielded, batch
            for result in batch:
                yield result
                yielded += 1
                if max_limit > 0 and yielded >= max_limit:
                    return

            print(f'Received {len(batch)} results')

            if len(batch) < increment:
                return

            while True:
                last = batch[len(batch) - 1]
                if last[search.sort[0].strip('+-')] is not None:
                    next_search_after = last[str(search.sort[0]).strip('+-')]
                    search.search_after = [next_search_after]
                else:
                    raise Exception('Search unexpectedly did not return a result we can search after!')

                print(f'Paginating call')
                batch = search_api.search_post_with_http_info(search, None, increment).data

                for result in batch:
                    yield result
                    yielded += 1
                    if max_limit > 0 and yielded >= max_limit:
                        return

                print(f'Received {len(batch)} results')

                if len(batch) < increment:
                    return

        return (first_response, _stream())

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