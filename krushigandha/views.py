from django.http import HttpResponse
from django.shortcuts import render, redirect
from contact.models import Contact
from carrier.models import Carrier
from django.contrib import messages
from django.utils import timezone
from order.models import Order  
from products.models import Product

def homePage(request):
    return render(request, "index.html")

def home(request):
    return render(request, "index.html")

def header(request):
    return render(request, "header.html")

def footer(request):
    return render(request, "footer.html")

def overview(request):
    context = {'name': 'overview'}
    return render(request, "overview.html", context)

def aboutCompany(request):
    context = {'name': 'aboutCompany'}
    return render(request, "aboutCompany.html", context)

def overview3(request):
    context = {'name': 'overview3'}
    return render(request, "overview3.html", context)

def benefit(request):
    context = {'name': 'benefit'}
    return render(request, "benefit.html", context)

def overall(request):
    context = {'name': 'overall'}
    return render(request, "overall.html", context)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product.html', {'products': products})

def gallary(request):
    context = {'name': 'gallary'}
    return render(request, "gallary.html", context)

def contact(request):
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        # Save data to the Contact model
        Contact.objects.create(
            username=username,
            email=email,
            mobile=mobile,
            message=message
        )

        # Redirect to a thank-you page or display success message
        return redirect('thank_you')  # Replace 'thank_you' with your URL pattern name

    context = {'name': 'contact'}
    return render(request, "contact.html", context)

def thank_you(request):
    return render(request, "thank_you.html")  # Create a `thank_you.html` template

def carrier(request):
    if request.method == 'POST':
        post = request.POST.get('post')
        experience = request.POST.get('experience')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')
        resume = request.FILES.get('resume')

        # Check if all required fields are filled out
        if not post or not experience or not name or not email or not mobile:
            messages.error(request, 'All fields are required!')
            return render(request, "carrier.html")

        try:
            # Save the form data to the database
            Carrier.objects.create(
                post=post,
                experience=experience,
                name=name,
                gender=gender,
                email=email,
                mobile=mobile,
                city=city,
                resume=resume,
                created_at=timezone.now()  # Manually set the current time if not using auto_now_add
            )
            messages.success(request, 'Resume submitted successfully!')

            # Redirect to the thank_you page after successful submission
            return redirect('thank_you')  # 'thank_you' is the URL name for the thank_you page

        except Exception as e:
            messages.error(request, f'Error submitting resume: {e}')

        # If there's an error, stay on the carrier form page
        return redirect('carrier')

    return render(request, "carrier.html")


def order(request):
    if request.method == 'POST':
        # Extract form data
        product_name = request.POST.get('productName')
        quantity = request.POST.get('quantity')
        customer_name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        whatsapp = request.POST.get('whatsapp')

        # Validate form data (basic validation example)
        if not product_name or not quantity or not customer_name or not address or not phone or not whatsapp:
            messages.error(request, 'All fields are required!')
            return redirect('order')  # Replace 'order' with the name of your URL pattern

        try:
            # Save order to the database
            Order.objects.create(
                product_name=product_name,
                quantity=quantity,
                customer_name=customer_name,
                address=address,
                phone=phone,
                whatsapp=whatsapp,
            )
            messages.success(request, 'Your order has been placed successfully!')

            # Redirect to order_done page
            return redirect('order_done')  # Redirect to the 'order_done' page

        except Exception as e:
            messages.error(request, f"Error placing order: {e}")
            return redirect('order')

    return render(request, "order.html")

def order_done(request):
    context = {'name': 'order_done'}
    return render(request, "order_done.html", context)

def profile(request):
    context = {'name': 'profile'}
    return render(request, "profile.html", context)