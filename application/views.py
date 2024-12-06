from .forms import ContactForm
from .models import Car
from .forms import CarForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Booking



def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def cars(request):
    return render(request, 'cars.html')

def team(request):
    return render(request, 'team.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def notfound(request):
    return render(request, 'notfound.html')  # Commonly named 404.html for consistency

def about(request):
    return render(request, 'about.html')

def feature(request):
    return render(request, 'feature.html')

def service(request):
    return render(request, 'service.html')

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'success.html')  # Redirect to success page
        else:
            # Render contact.html with errors
            return render(request, 'contact.html', {'form': form})
    else:
        # Render an empty form for GET requests
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})



def cars_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()  # Save only the submitted car instance
            return redirect('cars')  # Prevent resubmission on page refresh
    else:
        form = CarForm()

    cars = Car.objects.all()  # Fetch all unique car objects
    return render(request, 'cars.html', {'form': form, 'cars': cars})





def book_car(request, car_id):
    form = BookingForm()
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        # Extract form data
        pickup_location = request.POST.get('pickup_location')
        dropoff_location = request.POST.get('dropoff_location')
        pickup_date = request.POST.get('pickup_date')
        pickup_time = request.POST.get('pickup_time')
        dropoff_date = request.POST.get('dropoff_date')
        dropoff_time = request.POST.get('dropoff_time')

        # Calculate rental duration or amount
        # Example: Calculate duration in days
        pickup_datetime = datetime.combine(datetime.strptime(pickup_date, "%Y-%m-%d"),
                                           datetime.strptime(pickup_time, "%H:%M").time())
        dropoff_datetime = datetime.combine(datetime.strptime(dropoff_date, "%Y-%m-%d"),
                                            datetime.strptime(dropoff_time, "%H:%M").time())

        duration_days = (dropoff_datetime - pickup_datetime).days
        # Example: amount can be calculated based on car's daily rate
        daily_rate = car.daily_rate  # Assuming Car model has a 'daily_rate' field
        amount = duration_days * daily_rate

        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.car = car
            booking.amount = amount  # Set the calculated amount
            booking.save()
            return redirect('receipt', booking_id=booking.id)

        else:
            return render(request, 'book.html',
                          {'form': form, 'car': car})  # Render the index page with the booking form

    else:
        return render(request, 'book.html', {'form': form, 'car': car})



def receipt_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'receipt.html', {'booking': booking})