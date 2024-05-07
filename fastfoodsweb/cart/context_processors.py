from .models import Cart
from django.db.models import Q
from users.models import Profile

def cart(request):
    if request.user.is_authenticated:
            cartitems = Cart.objects.filter( Q(status="AD")|Q(status="CH"), customer=request.user.id,)
            cartqty = cartitems.count()
            cartChosen = cartitems.filter(status="CH").count()
            cartTotal = {}
            for item in cartitems:
                total = item.quantity*item.product.price
                cartTotal[item.id] = total
                
            grandtotal = 0
            for item in cartitems.filter(status="CH"):
                grandtotal += cartTotal[item.id]
            
            profile = Profile.objects.get(customer=request.user)
            rating = profile.rating
            discount = 1
            if rating > 80: discount = 0.9
            elif rating > 60: discount = 0.95
            else: pass
            
            grandtotal = int(grandtotal*discount)
            
            return {'cartqty': cartqty,
                    'cartitems': cartitems,
                    'carttotal': cartTotal,
                    'cartChosen': cartChosen,
                    'grandtotal': grandtotal,
                    }
    return {}


    
    