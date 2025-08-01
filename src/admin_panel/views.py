# admin_panel/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm 
# from django.contrib.auth.decorators import login_required, user_passes_test

# def is_admin(user):
#     return user.is_superuser 
# @login_required
# @user_passes_test(is_admin)
customers = Customer.objects.all()

def customers_view(request):
    
    return render(request, 'admin_panel/customers.html',{'customers': customers})

def delete_customer(request, customer_id):
    customer_obj = get_object_or_404(customers, id=customer_id)
    customer_obj.delete()
    return redirect('customers')



def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm()

    return render(request, 'admin_panel/add_customer.html', {'form': form})

def products_view(request):
    return render(request,'admin_panel/products.html')