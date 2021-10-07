from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = "size"
    page_size = 3

    def get_paginated_response(self, data):
        return Response(
            {
                "total": self.page.paginator.count,
                "count": len(data),
                "current_page": self.page.number,
                "pages": self.page.paginator.num_pages,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "data": data,
            }
        )


class QuizPagination(CustomPagination):
    page_size = 5


class CategoryPagination(CustomPagination):
    page_size = 3
