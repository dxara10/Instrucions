class MeuMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Código executado antes da view ser chamada
        response = self.get_response(request)
        # Código executado após a view ser chamada
        return response
