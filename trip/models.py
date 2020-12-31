import uuid
from django.db import models

class TripRequest(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	reference_number = models.CharField(max_length=255, unique=True)
	status = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.reference_number)

class TripLoading(models.Model):
	# start trip loading details
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	process_request = models.ForeignKey(
		TripRequest, on_delete=models.CASCADE,
		related_name = 'trip_loading_details'
	)
	buying_price_per_kg = models.CharField(max_length=255)
	total_weight_bought = models.CharField(max_length=255)
	total_buying_price = models.CharField(max_length=255)
	loading_cost = models.CharField(max_length=255)
	departure_date = models.DateField()

	class Meta:
		verbose_name_plural = "loading details"

	def __str__(self):
		return str(self.process_request.title)


class TripOffloading(models.Model):
	# End Trip offloading details
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	process_request = models.ForeignKey(
		TripRequest, on_delete=models.CASCADE,
		related_name='trip_offloading_details'
	)

	selling_price_per_kg = models.CharField(max_length=255)
	total_weight_sold = models.CharField(max_length=255)
	total_selling_price = models.CharField(max_length=255)
	offloading_cost = models.CharField(max_length=255)
	selling_date = models.DateField()

	class Meta:
		verbose_name_plural = "offloading details"

	def __str__(self):
		return str(self.process_request.title)

class TripExpense(models.Model):
	# Trip expenses details
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	process_request = models.ForeignKey(
		TripRequest, on_delete=models.CASCADE,
		related_name='trip_expense_details'
	)
	transport_cost = models.CharField(max_length=255)
	clearance_cost = models.CharField(max_length=255)
	broker_cost = models.CharField(max_length=255)
	total_expense = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural = "expense details"

	def __str__(self):
		return str(self.process_request.title)

class TripShare(models.Model):
	# Trip share details
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	process_request = models.ForeignKey(
		TripRequest, on_delete=models.CASCADE,
		related_name="trip_profit_share"
	)
	user = models.CharField(max_length=255)
	profit_share = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural = "shares details"
		
	def __str__(self):
		return str(self.process_request.title)
	
