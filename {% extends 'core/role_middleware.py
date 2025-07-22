from django.shortcuts import redirect

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.path.startswith('/admin/') and request.user.role != 'admin':
                return redirect('dashboard')
        return self.get_response(request)
