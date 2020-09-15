import uuid
from django.db import models

class Trip(models.Model):
	# id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=200, unique=True, help_text='Enter a unique name for the Trip') #user input
	created_on = models.DateField() #user input

	def __str__(self):
		return self.title

class Loading(models.Model):
	# loading details
	# id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	trip = models.OneToOneField(Trip, on_delete=models.CASCADE, blank=False)
	buying_price_per_kg = models.DecimalField(max_digits=8, decimal_places=2) #user input
	total_weight_bought = models.IntegerField(default=0, help_text='Enter the total weight bought') #user input
	total_buying_price = models.DecimalField(max_digits=8, decimal_places=2,default=1)
	loading_cost = models.DecimalField(max_digits=8, decimal_places=2) #user input
	departure_date = models.DateField() #user input

	comment = models.TextField(default='Enter comment if any',blank=True) #user input

	class Meta:
		verbose_name_plural = "Loading Details"

	def get_total_buying_price(self):
		return self.buying_price_per_kg * self.total_weight_bought

	def get_loading_expense(self):
		return self.loading_cost + self.get_total_buying_price()

	def __str__(self):
		return self.trip.title

	def save(self, *args, **kwargs):
		self.total_buying_price = self.get_total_buying_price()
		super(Loading, self).save(*args, **kwargs)


class Offloading(models.Model):
	# offloading details
	# id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	trip = models.OneToOneField(Trip, on_delete=models.CASCADE, blank=False)
	loading = models.OneToOneField(Loading, on_delete=models.CASCADE, blank=False)
	selling_price_per_kg = models.DecimalField(max_digits=8, decimal_places=2) #user input
	total_weight_sold = models.IntegerField(default=0, help_text='Enter the total weight sold') #user input
	total_selling_price = models.DecimalField(max_digits=8, decimal_places=2,default=1)
	offloading_cost = models.DecimalField(max_digits=8, decimal_places=2) #user input
	selling_date = models.DateField() #user input

	comment = models.TextField(default='Enter comment if any',blank=True) #user input

	class Meta:
		verbose_name_plural = "Offloading Details"

	def get_total_selling_price(self):
		return self.selling_price_per_kg * self.total_weight_sold

	def __str__(self):
		return self.trip.title

	def save(self, *args, **kwargs):
		self.total_selling_price = self.get_total_selling_price()
		super(Offloading, self).save(*args, **kwargs)


class TripInfo(models.Model):
	# trip details
	# id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	trip = models.OneToOneField(Trip, on_delete=models.CASCADE, blank=False,related_name='tripInfo')
	loading = models.OneToOneField(Loading, on_delete=models.CASCADE, related_name='loading')
	offloading = models.OneToOneField(Offloading, on_delete=models.CASCADE, related_name='offloading')

	transport_cost = models.DecimalField(max_digits=8, decimal_places=2, default=80000) #user input
	clearance_cost = models.DecimalField(max_digits=8, decimal_places=2, default=9000) #user input
	broker_expenses = models.DecimalField(max_digits=8, decimal_places=2) #user input
	total_expenses = models.DecimalField(max_digits=8, decimal_places=2,default=1)
	profit_margin = models.DecimalField(max_digits=8, decimal_places=2,default=1)

	comment = models.TextField(default='Enter comment if any',blank=True) #user input

	class Meta:
		verbose_name_plural = "Trip Details"

	def __str__(self):
		return self.trip.title

	def get_total_expenses(self):
		return (self.loading.get_loading_expense() 
			+ self.offloading.offloading_cost 
			+ self.transport_cost + self.clearance_cost 
			+ self.broker_expenses)
	
	def get_profit_margin(self):
		return (self.offloading.total_selling_price - self.get_total_expenses())

	def save(self, *args, **kwargs):
		self.total_expenses = self.get_total_expenses()
		self.profit_margin = self.get_profit_margin()
		super(TripInfo, self).save(*args, **kwargs)