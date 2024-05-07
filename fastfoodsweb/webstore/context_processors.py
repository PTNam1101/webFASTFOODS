from .models import Category, Product
from users.models import Profile
def menu(request):
    categories = []
    for cate in Category.objects.all().exclude(name="Combo"):
        if Product.objects.filter(category = cate).exists():
            categories.append(cate.id) 
            
    return {'categories': Category.objects.filter(id__in=categories),
            'products': Product.objects.all().order_by('-ordered_times'),
            }
    
def combo(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(customer = request.user)
        combos = Product.objects.filter(combo = True)
        rating = profile.rating
        combos = combos.filter(min_user_rating__lte=rating)
        return {'combos': combos,}
    return {}