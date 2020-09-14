from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

class Task(models.Model):
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False, blank=True, null=True)
			
	def __str__(self):
		return self.title


class TripInfo(models.Model):
	title = models.CharField(max_length=200) #user input

	# loading details
	buying_price_per_kg = models.DecimalField(max_digits=8, decimal_places=2) #user input
	total_weight_bought = models.IntegerField(default=0, help_text='Enter the total weight bought') #user input
	total_buying_price = models.DecimalField(max_digits=8, decimal_places=2,default=1)
	loading_cost = models.DecimalField(max_digits=8, decimal_places=2) #user input
	departure_date = models.DateField() #user input

	# offloading details
	selling_price_per_kg = models.DecimalField(max_digits=8, decimal_places=2) #user input
	total_weight_sold = models.IntegerField(default=0, help_text='Enter the total weight sold') #user input
	total_selling_price = models.DecimalField(max_digits=8, decimal_places=2,default=1)
	offloading_cost = models.DecimalField(max_digits=8, decimal_places=2) #user input
	selling_date = models.DateField() #user input

	
	# trip details
	transport_cost = models.DecimalField(max_digits=8, decimal_places=2, default=80000) #user input
	clearance_cost = models.DecimalField(max_digits=8, decimal_places=2, default=9000) #user input
	broker_expenses = models.DecimalField(max_digits=8, decimal_places=2) #user input
	total_expenses = models.DecimalField(max_digits=8, decimal_places=2,default=1)
	profit_margin = models.DecimalField(max_digits=8, decimal_places=2,default=1)

	comment = models.TextField(blank=True) #user input

	class Meta:
		verbose_name_plural = "Trip_info"


	def get_total_buying_price(self):
			return self.buying_price_per_kg * self.total_weight_bought

	def get_total_selling_price(self):
		return self.selling_price_per_kg * self.total_weight_sold

	def get_total_expenses(self):
		result = self.total_buying_price + self.loading_cost + self.offloading_cost + self.transport_cost + self.clearance_cost + self.broker_expenses
		return result
	
	def get_profit_margin(self):
		return (self.total_selling_price - self.get_total_expenses())

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
			self.total_buying_price = self.get_total_buying_price()
			self.total_selling_price = self.get_total_selling_price()
			self.total_expenses = self.get_total_expenses()
			self.profit_margin = self.get_profit_margin()
			super(TripInfo, self).save(*args, **kwargs)