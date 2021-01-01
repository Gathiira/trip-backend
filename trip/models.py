import uuid
from django.db import models

class TripRequest(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	reference_number = models.CharField(max_length=255, unique=True)
	status = models.CharField(max_length=255)
	total_expense = models.FloatField(null=True, blank=True, editable=False)
	profit_margin = models.FloatField(null=True, blank=True, editable=False)
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
	buying_price_per_kg = models.FloatField()
	total_weight_bought = models.FloatField()
	total_buying_price = models.FloatField(null=True, blank=True, editable=False)
	loading_cost = models.FloatField()
	departure_date = models.DateField()

	class Meta:
		verbose_name_plural = "loading details"

	def __str__(self):
		return str(self.process_request.reference_number)


class TripOffloading(models.Model):
	# End Trip offloading details
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	process_request = models.ForeignKey(
		TripRequest, on_delete=models.CASCADE,
		related_name='trip_offloading_details'
	)

	selling_price_per_kg = models.FloatField()
	total_weight_sold = models.FloatField()
	total_selling_price = models.FloatField(null=True, blank=True, editable=False)
	offloading_cost = models.FloatField()
	selling_date = models.DateField()

	class Meta:
		verbose_name_plural = "offloading details"

	def __str__(self):
		return str(self.process_request.reference_number)

class TripExpense(models.Model):
	# Trip expenses details
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	process_request = models.ForeignKey(
		TripRequest, on_delete=models.CASCADE,
		related_name='trip_expense_details'
	)
	transport_cost = models.FloatField()
	clearance_cost = models.FloatField()
	broker_cost = models.FloatField()

	class Meta:
		verbose_name_plural = "expense details"

	def __str__(self):
		return str(self.process_request.reference_number)

class TripShare(models.Model):
	# Trip share details
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	process_request = models.ForeignKey(
		TripRequest, on_delete=models.CASCADE,
		related_name="trip_profit_share"
	)
	user = models.CharField(max_length=255)
	profit_share = models.FloatField(null=True, blank=True, editable=False)

	class Meta:
		verbose_name_plural = "shares details"
		
	def __str__(self):
		return str(self.process_request.reference_number)
	
