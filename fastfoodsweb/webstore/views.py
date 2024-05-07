from django.shortcuts import render, redirect
from .models import *
   
def searched(request):
   if request.method == 'POST':
      searched = request.POST["search"]
      searchresult = Product.objects.filter(name__contains=searched).exclude(combo=True)
      return render(request, 'search.html',
                    {'searched': searched, 
                     'searchresult' : searchresult,
                     })
   else:
      return render(request, 'homepage.html',{})
  
def homepage(request):
    if request.user.is_authenticated:
        user = request.user
        context={
            'user': user
        }
    else: context={}
    return render(request, 'homepage.html',context)

def allInCategory(request, pk):
    productC = Product.objects.filter(category=pk)
    category = Category.objects.get(id=pk)
    context = {
        'productC': productC,
        'category': category,
    } 
    return render(request, 'category.html', context)

def about(request):
    return render(request, 'aboutus.html', {})