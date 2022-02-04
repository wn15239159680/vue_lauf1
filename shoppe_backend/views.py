from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

class Index(APIView):

    def get(self, request):
        res = Response({"code":200, "msg":"laufing"})
        res.set_cookie("name", "laufing", max_age=300)
        return res

