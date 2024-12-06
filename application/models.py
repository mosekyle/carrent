from decimal import Decimal

# Create your models here.
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    project = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"



class Car(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars/')  # Updated field for uploaded images
    review_score = models.FloatField()
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    seats = models.PositiveIntegerField()
    transmission = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    engine = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50)

    def __str__(self):
        return self.name





class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)  # Ensure this field is in your model
    dropoff_location = models.CharField(max_length=100)  # Ensure this field is in your model
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    dropoff_date = models.DateField()
    dropoff_time = models.TimeField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Booking for {self.car}"

# Receipt model, with additional fields and logic for handling amount and payment methods
class Receipt(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='receipt')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Receipt for {self.booking.car_type} - {self.amount}"

    # Method to calculate total price including any taxes or discounts
    def calculate_total(self):
        # Assuming 'amount' is the base price, we can apply tax and discounts here
        tax_rate = Decimal('0.10')  # 10% tax
        discount_rate = Decimal('0.05')  # 5% discount

        # Apply tax
        tax = self.amount * tax_rate
        # Apply discount
        discount = self.amount * discount_rate

        # Calculate total amount
        total_amount = self.amount + tax - discount
        return total_amount

    # Method to calculate tax
    def calculate_tax(self):
        return self.amount * Decimal('0.10')  # 10% tax

    # Method to calculate discount
    def calculate_discount(self):
        return self.amount * Decimal('0.05')  # 5% discount

    # Method to update receipt
    def update_receipt(self, new_amount, new_payment_method):
        self.amount = new_amount
        self.payment_method = new_payment_method
        self.save()

    # Delete the receipt (if needed)
    def delete_receipt(self):
        self.delete()