import uuid
from django.db import models

class TripLoading(models.Model):
	# start trip loading details
	# id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=200, unique=True, help_text='Enter a unique name for the Trip') #user input

	buying_price_per_kg = models.DecimalField(max_digits=8, decimal_places=2) #user input
	total_weight_bought = models.IntegerField(default=0, help_text='Enter the total weight bought') #user input
	total_buying_price = models.DecimalField(max_digits=8, decimal_places=2,default=1)
	loading_cost = models.DecimalField(max_digits=8, decimal_places=2) #user input
	departure_date = models.DateField() #user input

	comment = models.TextField(default='Enter comment if any',blank=True) #user input

	class Meta:
		verbose_name_plural = "Start Trip Loading Details"

	def get_total_buying_price(self):
		return self.buying_price_per_kg * self.total_weight_bought

	def get_loading_expense(self):
		return self.loading_cost + self.get_total_buying_price()

	def __str__(self):
		return 'loading '+self.title

	def save(self, *args, **kwargs):
		self.total_buying_price = self.get_total_buying_price()
		super(TripLoading, self).save(*args, **kwargs)


class TripOffloading(models.Model):
	# End Trip offloading details
	# id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	trip_loading = models.OneToOneField(TripLoading, on_delete=models.CASCADE, blank=False, related_name='trip_offloading')

	transport_cost = models.DecimalField(max_digits=8, decimal_places=2, default=80000) #user input
	clearance_cost = models.DecimalField(max_digits=8, decimal_places=2, default=9000) #user input

	selling_price_per_kg = models.DecimalField(max_digits=8, decimal_places=2) #user input
	total_weight_sold = models.IntegerField(default=0, help_text='Enter the total weight sold') #user input
	total_selling_price = models.DecimalField(max_digits=8, decimal_places=2,default=1)
	offloading_cost = models.DecimalField(max_digits=8, decimal_places=2) #user input
	selling_date = models.DateField() #user input

	broker_expenses = models.DecimalField(max_digits=8, decimal_places=2) #user input
	total_expenses = models.DecimalField(max_digits=8, decimal_places=2,default=1)
	profit_margin = models.DecimalField(max_digits=8, decimal_places=2,default=1)

	comment = models.TextField(default='Enter comment if any',blank=True) #user input

	class Meta:
		verbose_name_plural = "End Trip Offloading Details"

	def get_total_selling_price(self):
		return self.selling_price_per_kg * self.total_weight_sold

	def __str__(self):
		return 'Offloading '+self.trip_loading.title

	def get_total_expenses(self):
		return (self.trip_loading.get_loading_expense() 
			+ self.offloading_cost 
			+ self.transport_cost + self.clearance_cost 
			+ self.broker_expenses)
	
	def get_profit_margin(self):
		return (self.total_selling_price - self.get_total_expenses())

	def save(self, *args, **kwargs):
		self.total_selling_price = self.get_total_selling_price()
		self.total_expenses = self.get_total_expenses()
		self.profit_margin = self.get_profit_margin()
		super(TripOffloading, self).save(*args, **kwargs)