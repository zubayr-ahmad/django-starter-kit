from rest_framework.pagination import PageNumberPagination

class PageLimitPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 1000

def paginate(queryset, request, serializer_class):

    pagination_class = PageLimitPagination()
    paginated_queryset = pagination_class.paginate_queryset(
            queryset=queryset, request=request
        )
    serializer = serializer_class(
        paginated_queryset, many=True
    )
    paginated_data = {
        'count': queryset.count(),
        'next': pagination_class.get_next_link(),
        'previous': pagination_class.get_previous_link(),
        'results': serializer.data
    }
    return paginated_data
