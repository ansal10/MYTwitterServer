
import random
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def ola_bill(request):
	# Content to be edited
	driver_name = "Anas"
	travel_date = "20 March, 2017"
	from_time = "10:01 AM"
	to_time = "10:53 AM"
	car_name = "Micro - White hyundai i10"
	order_id = "CRN614998301"
	base_fare = 185
	from_location = None  # fill when dont want to use default location
	to_location = None    # fill when dont want to use default location

	office_to_hindon = False  # Set True or False 

	if from_location is None and to_location is None:
		if office_to_hindon:
			from_location = "56a, Bishanpura Main Rd, Khora Colony, Sector 62, Noida"
			to_location = "Unnamed Road, Hindon Air Force Station, Hindon Residential Area, Ghaziabad"
		else:
			to_location = "56a, Bishanpura Main Rd, Khora Colony, Sector 62, Noida"
			from_location = "Unnamed Road, Hindon Air Force Station, Hindon Residential Area, Ghaziabad"


	# Contents with no editing required

	base_fare = base_fare + round(random.uniform(1,3),2)
	tax_rate = 7.6
	taxes = round((tax_rate * base_fare)/100.0,2)

	total_amount = int(base_fare + taxes)

	data = {
		"driver_name": driver_name,
		"travel_date": travel_date,
		"from_time": from_time,
		"to_time": to_time,
		"from_location": from_location,
		"to_location": to_location,
		"base_fare": base_fare,
		"taxes": taxes,
		"total_amount": total_amount,
		"order_id": order_id,
		"car_name": car_name,
	}
	return render(request, 'bills/ola.html', data)


def map_from_delhi(request):
	with open('/Userstatic/from_delhi', "rb") as f:
		return HttpResponse(f.read(), content_type="image/jpeg")
