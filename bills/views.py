from random import randint

from django.shortcuts import render


# Create your views here.
def ola_bill(request):


	# Content to be edited
	driver_name = "Balweer Singh"
	travel_date = "12 Feb, 2017"
	distance = 14.1
	travel_time = 65
	from_time = "06:30 PM"
	to_time = "08:30 PM"
	from_location = "Asotech One, C Block, Phase 2, Industrial Area, Sector 62, Noida, Uttar Pradesh 201307, India"
	to_location = "Maharani Bagh, New Friends Colony, New Delhi, Delhi"
	driver_image = "https://scontent.fdel6-1.fna.fbcdn.net/v/t1.0-1/p320x320/16708277_1882962878581953_731439520810060991_n.jpg?oh=022b20160bb06893cec0d640b0eb24f1&oe=5954BC4E"
	#Content till when edited allowed

	car_name = "Micro - White Swift Dzire"



	from_noida = False
	if 'delhi' in to_location.lower():
		from_noida = True

	state_tax = True
	if not from_noida:
		state_tax = False
		x = from_location
		from_location = to_location
		to_loc = "Mindfire solutions, Noida, Uttar Pradesh"


	base_fare = 40
	km_charge = 6
	distance_fare = km_charge * distance
	total_base_fare = base_fare + distance_fare + travel_time
	taxes = round((10.71*total_base_fare)/100.0, 1)
	total_amount = taxes + total_base_fare + ( 100 if state_tax else 0)
	order_id = "CRN55"+ randint(7000000, 9999999).__str__()

	data = {
		"driver_name": driver_name,
		"travel_date": travel_date,
		"travel_time": 63,
		"from_noida": from_noida,
		"from_time": from_time,
		"to_time": to_time,
		"from_location": from_location,
		"to_location": to_location,
		"state_tax": state_tax,
		"base_fare": base_fare,
		"distance_fare": distance_fare,
		"total_base_fare": total_base_fare,
		"taxes": taxes,
		"total_amount": total_amount,
		"order_id": order_id,
		"distance": distance,
		"car_name": car_name,
		"driver_image": driver_image

	}
	return render(request, 'bills/ola.html', data)

