from .models import Profile

def profile(request):
    if request.user.is_authenticated:
        return {'profile': Profile.objects.get(customer=request.user)}
    return{}