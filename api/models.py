import uuid
from django.db import models

from accounts.models import Member

class TripLoading(models.Model):
	# start trip loading details
	# id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=200, unique=True, help_text='Enter a unique name for the Trip') #user input

	buying_price_per_kg = models.DecimalField(max_digits=19,decimal_places=2,default=1) #user input
	total_weight_bought = models.DecimalField(max_digits=19,decimal_places=2,default=1, help_text='Enter the total weight bought') #user input
	total_buying_price = models.DecimalField(max_digits=19,decimal_places=2,default=1, editable=False)
	loading_cost = models.DecimalField(max_digits=19,decimal_places=2, default=1) #user input
	departure_date = models.DateField() #user input

	comment = models.TextField(default='Enter comment if any',blank=True) #user input

	class Meta:
		verbose_name_plural = "Loading Details"

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
	trip_loading = models.OneToOneField(TripLoading, on_delete=models.CASCADE, blank=False, related_name='trip_offloading') # user select

	transport_cost = models.DecimalField(max_digits=19,decimal_places=2, default=80000) #user input
	clearance_cost = models.DecimalField(max_digits=19,decimal_places=2, default=9000) #user input

	selling_price_per_kg = models.DecimalField(max_digits=19,decimal_places=2) #user input
	total_weight_sold = models.DecimalField(max_digits=19,decimal_places=2,default=1, help_text='Enter the total weight sold') #user input
	total_selling_price = models.DecimalField(max_digits=19,decimal_places=2,default=1,editable=False)
	offloading_cost = models.DecimalField(max_digits=19,decimal_places=2) #user input
	selling_date = models.DateField() #user input

	broker_expenses = models.DecimalField(max_digits=19,decimal_places=2) #user input
	total_expenses = models.DecimalField(max_digits=19,decimal_places=2,default=1,editable=False)
	profit_margin = models.DecimalField(max_digits=19,decimal_places=2,default=1,editable=False)

	comment = models.TextField(default='Enter comment if any',blank=True) #user input

	class Meta:
		verbose_name_plural = "Offloading Details"

	def get_total_selling_price(self):
		return self.selling_price_per_kg * self.total_weight_sold

	def __str__(self):
		return 'Offloading '+ self.trip_loading.title

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

class SharesModel(models.Model):
	offloading = models.ForeignKey(TripOffloading, on_delete=models.DO_NOTHING,related_name="profits")
	user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='name')
	profit_share = models.DecimalField(max_digits=19, decimal_places=2, default=1) #, editable=False

	def __unicode__(self):
		return '%s: %s' % (self.user.username, self.profit_share)

	def get_profit_share(self):
		return (
			(float(self.user.percentage) * 0.01) * float(self.offloading.profit_margin)
		)
	
	def __str__(self):
		return self.user.username +' profit for ' + self.offloading.trip_loading.title

	def save(self, *args, **kwargs):
		self.profit_share = self.get_profit_share()
		super(SharesModel, self).save(*args, **kwargs)
