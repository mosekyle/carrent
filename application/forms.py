from django import forms
from .models import ContactMessage
from .models import Car
from .models import Booking
from django import forms
from .models import Receipt

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['car', 'pickup_location', 'dropoff_location', 'pickup_date', 'pickup_time', 'dropoff_date', 'dropoff_time']

    car = forms.ModelChoiceField(queryset=Car.objects.all(), empty_label="Select Your Car Type", widget=forms.Select(attrs={'class': 'form-select'}))
    pickup_location = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a City or Location'}))
    dropoff_location = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a City or Location'}))
    pickup_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    pickup_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    dropoff_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    dropoff_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'project', 'subject', 'message']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'image', 'review_score', 'daily_rate', 'seats', 'transmission', 'fuel', 'year', 'engine', 'mileage']


