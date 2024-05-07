from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, Address, Order
from webstore.models import Product
from django.db.models import Q
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from users.models import Profile
from django.contrib.auth import authenticate, login, logout

def cart_inventory(request):
    addresses = Address.objects.filter(customer=request.user)
    profile = Profile.objects.get(customer=request.user)
    rating = profile.rating
    discount = "0%"
    adc = 1
    if rating > 80: 
        discount = "10%"
        adc = 0.9
    elif rating > 60: 
        discount = "5%"
        adc = 0.95
    
    else: pass
    
    return render(request,'cart_inventory.html',{'addresses': addresses, 'discount': discount,'adc':adc})

def cart_add(request):
    if request.user.is_authenticated:
        if request.POST.get('action') == 'post':            
            product_id = int(request.POST.get('product_id'))
            product = Product.objects.get(id=product_id)
            
            user = request.user
            #Lay cart chua product vua chon cua user neu chua co thi tao voi quantity = 0
            user_cart_items, create = Cart.objects.filter(Q(status="AD")|Q(status="CH"),customer=user,product=product).get_or_create(customer=user,product=product,status="AD")
            #Quantity +1
            if user_cart_items:
                user_cart_items.quantity += 1
                user_cart_items.save()
            elif create:
                create.quantity +=1
                create.save()
            cartqty = Cart.objects.filter( Q(status="AD")|Q(status="CH"), customer=request.user.id).count()
            response = JsonResponse({'qty': cartqty })
            return response
    else:
        messages.success(request, ("Bạn phải đăng nhập để đặt hàng"))
        return render(request, 'homepage.html',{})
    
def cart_update_qty(request):
    if request.POST.get('action') == 'post':
        cart_id = int(request.POST.get('cart_id'))
        cart_qty = int(request.POST.get('cart_qty'))
        
        cart = Cart.objects.get(id=cart_id)
        change = 0
        if cart.status == "CH":
            change = cart_qty - cart.quantity  
        cart.quantity = cart_qty
        cart.save()
        
        response = JsonResponse({'qty': cart.quantity,
                                 'change': change,
                                 })
        return response
    
def cart_delete(request):
    if request.POST.get('action') == 'post':
        cart_id = int(request.POST.get('cart_id'))
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        cartqty = Cart.objects.filter( Q(status="AD")|Q(status="CH"), customer=request.user.id).count()
        response = JsonResponse({'cart_id': cart_id,'qty': cartqty, })
        
        return response
    
def cart_update_status(request):
    if request.POST.get('action') == 'post':
        cart_id = int(request.POST.get('cart_id'))
        cart_status = request.POST.get('cart_status')
        cart = Cart.objects.get(id=cart_id)
        if cart_status == "AD":
            cart.status = "CH"
        else:
            cart.status = "AD"
            
        cart.save()
        response = JsonResponse({'status': cart.status })
        return response
    
def create_order(request):
     if request.method == 'POST':
        customer = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(customer=customer)
        rating = profile.rating 
        cart = Cart.objects.filter(customer=customer, status="CH")
        receiver = request.POST["receiver"]
        address = request.POST["address"]
        phonenum = request.POST["phonenum"]
        ordernote = request.POST["ordernote"]
        
        orderdate = str(datetime.now())
        
        # orderdate = timezone.now()
        # messages.success(request, (str(orderdate)))
        
        # orderdatetime = datetime.strptime(orderdatetime,"YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
        
        total = 0
        discount = 1
        for c in cart:
            total += c.product.price*c.quantity
            c.status = "OR"
        if rating > 80: discount = 0.9
        elif rating > 60: discount = 0.95
        else: discount = 1
    
        total = int(total*discount)
        order = Order(customer=customer, address=address, receiver=receiver, phone=phonenum, note=ordernote, orderedTime=orderdate, total=total)
        order.save()
        for c in cart:
            c.order = order
            c.save()
            
        messages.success(request, ("Đơn hàng được tạo thành công bạn có thể xem đơn hàng tại trang thông tin tài khoản."))
        return redirect('homepage')
    
def add_address(request):
    if request.method == 'POST':
        customer = request.user
        ads = Address.objects.filter(customer=customer)
        address = request.POST["address"]
        if ads.filter(address__contains=address):
            messages.success(request, ("Địa chỉ này trùng với địa chỉ đã có, hãy thêm địa chỉ khác"))
            return redirect('profile')
        if ads.count() >= 5:
            messages.success(request, ("Bạn đã lưu 5 địa chỉ hãy xóa bớt 1 địa chỉ để thêm địa chỉ mới."))
            return redirect('profile')         
        ad = Address(customer=customer, address=address)
        ad.save()
        messages.success(request, ("Thêm địa chỉ mới thành công hãy click vào địa chỉ để đặt làm mặc định"))
        return redirect('profile')
    
def update_address(request, addid):
    ads = Address.objects.filter(customer = request.user)
    default_ad = ads.get(id = addid)
    for ad in ads:
        if ad.default == True and ad.id != addid:
            ad.default = False
            ad.save()
    default_ad.default = True
    default_ad.save()
    messages.success(request, ("Cập nhật địa chỉ mặc định thành công!"))
    return redirect('profile')
    
    
def update_profile(request):
    if request.method == 'POST':
        customer = request.user
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        
        customer.first_name = fullname
        customer.email = email
        customer.save()
        profile = Profile.objects.get(customer = customer)
        profile.phonenum = phone
        profile.save()
        return redirect('profile')
    
def order_detail(request, order_id):
    if request.user.is_authenticated:
        order= Order.objects.get(id=order_id)
        if order.customer == request.user:
            cartitems = Cart.objects.filter(order=order)
            cartCount = cartitems.count()
            OcartTotal = {}
            for item in cartitems:
                total = item.quantity*item.product.price
                OcartTotal[item.id] = total
            
            status = order.status
            minuspoint = 0
            if status == 'CE':
                status = 'Chờ xác nhân'
                minuspoint = 0
            elif status == 'PR':
                status = 'Chuẩn bị'
                minuspoint = int(order.total/100000)*10
                if minuspoint == 0:
                    minuspoint = 5
            elif status == 'DE':
                status = 'Đang giao'
                minuspoint = int(order.total/100000)*15
                if minuspoint == 0:
                    minuspoint = 10
            
            profile = Profile.objects.get(customer=request.user)
            resultrating = profile.rating - minuspoint
            if resultrating < 0:
                resultrating = 0
                
            context = {'order': order,
                    'cartitems': cartitems,
                    'cartcount': cartCount,
                    'OcartTotal': OcartTotal,
                    'minuspoint': minuspoint,
                    'resultrating': resultrating,
                    'status': status,
                    }                   
            return render(request,'orderdetail.html', context)
        return redirect('homepage')
    return redirect('homepage')
    
def order_cancel(request, order_id):
    if request.user.is_authenticated:
        order= Order.objects.get(id=order_id)
        if order.customer == request.user:
            user = order.customer
            status = order.status
            minuspoint = 0
            if status == 'CE':
                minuspoint = 0
            elif status == 'PR':
                minuspoint = int(order.total/100000)*10
                if minuspoint == 0:
                    minuspoint = 5
            elif status == 'DE':
                minuspoint = int(order.total/100000)*15
                if minuspoint == 0:
                    minuspoint = 10
            
            profile = Profile.objects.get(customer=user)
            resultrating = profile.rating - minuspoint
            if resultrating <= 0:
                resultrating = 0
                user.is_active = False
                user.save()
            profile.rating = resultrating
            profile.save()
            
            cartitems = Cart.objects.filter(order=order)
            for item in cartitems:
                item.status = "CA"
                item.save()
                
            order.status = "CA"
            order.save()   
            
            if resultrating == 0:
                logout(request)
                messages.success(request, ("Điểm của bạn về đã về  0 tài khoản tạm thời bị khóa hãy liên hệ với FASTFOODSWEB để biết thêm chi tiết."))
                return redirect('homepage')
            
            messages.success(request, ("Bạn đã hủy đơn thành công điểm còn lại là " + str(resultrating) + ". Hãy đặt nhiều đơn thành công hơn để tăng điểm và nhận ưu đãi nha"))            
            return redirect('profile')
        return redirect('homepage')
    return redirect('homepage')