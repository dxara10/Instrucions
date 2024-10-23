from django.views import View
from django.http import HttpResponse

class MinhaView(View):
    def get(self, request):
        return HttpResponse('Olá, mundo! Esta é uma view baseada em classes.')
