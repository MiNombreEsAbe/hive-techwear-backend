from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response

class CustomizePaging(pagination.PageNumberPagination):

    def get_paging_response(self, data):
        if not data:
            pages = 0
        else:
            pages = self.page.paginator.num_pages

        return Response({
            'count': self.page.paginator.count,
            'pages': pages,
            'current': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

# add to rest_framework in settings.py 
#   'DEFAULT_PAGINATION_CLASS': 'config.paging.CustomizePaging',
#   'PAGE_SIZE': 8