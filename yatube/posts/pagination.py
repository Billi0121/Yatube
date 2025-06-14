from rest_framework import pagination
from rest_framework.response import Response
from .models import *

class CustomPagination(pagination.BasePagination):

    def paginate_queryset(self, queryset, request, view=None):
        queryset = Post.objects.all()[:10]
        return queryset

    def get_paginated_response(self, data):
        return Response({
            'result': data
        })