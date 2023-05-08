from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPager(PageNumberPagination):
    """
        A simple page number based style that supports page numbers as
        query parameters. For example:

        http://api.example.org/accounts/?page=4
        http://api.example.org/accounts/?page=4&page_size=100
        """
    # The default page size.
    # Defaults to `None`, meaning pagination is disabled.
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = None
    max_page_size = None
