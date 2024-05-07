from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.forms.utils import ErrorList
from .models import Profile
from cart.models import Address, Order
from cart.models import Cart
from django.db.models import Q
from users.models import Profile
# Create your views here.

def login_user(request):
    context = {
    }
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["userpassword"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Chào mừng trở lại "+ user.first_name))
            return redirect('homepage')
            
        else:
            messages.success(request, ("Tên đăng nhập hoặc mật khẩu không đúng, vui lòng nhập lại!"))
            return redirect('login')
        # Return an 'invalid login' error message.
        
    else:
        return render(request, 'auth/login.html',context)
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Đăng xuất thành công"))
    return redirect('homepage')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            profile = Profile()
            profile.customer = user
            profile.save()
            messages.success(request, ("Tài khoản đã tạo thành công giờ bạn có thể đặt mua các món ăn!!!"))
            return redirect('homepage')
        # else:
        #     messages.success(request, ("Thông tin bạn nhập không hợp lệ, vui lòng nhập lại"))
        #     return redirect('register')
        
    else:
        form = RegisterUserForm()
        
    context = {
        'form': form,
    }
    return render(request, 'auth/register.html',context)

def profile_user(request):
    profile,state = Profile.objects.get_or_create(customer=request.user)
    if state:
        messages.success(request, ("Bạn có thể xem và sửa thông tin cá nhân tại đây và xem các đơn hàng của bạn"))
        
    addresses = Address.objects.filter(customer=request.user)
    orders = Order.objects.filter(customer=request.user).order_by('-id')
    ordersCount = orders.count()
    orderCE = orders.filter(status="CE").count()
    orderPR = orders.filter(status="PR").count()
    orderDE = orders.filter(status="DE").count()
    orderDR = orders.filter(status="DR").count()
    orderCA = orders.filter(status="CA").count()
    
    
    context = {
        'addresses': addresses,
        'ordersCount': ordersCount,
        'orders': orders,
        'orderCE': orderCE,
        'orderPR': orderPR,
        'orderDE': orderDE,
        'orderDR': orderDR,
        'orderCA': orderCA,
    }
    return render(request, 'auth/profile.html', context)

