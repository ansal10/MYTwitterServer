
import random
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def ola_bill(request):
	office_to_hindon_map = "https://ci4.googleusercontent.com/proxy/WRAN3c_BAdP4Grq_tqb0Vrupy6kRiCmUh6ZW59ruyeg2tMyGkLcPZYFs3yezQL_k43LERPUBF8gC67BJtGdeOMp-2mHPIONOBHMRzGFxggx_zakHR2o58y_aujEp-OJc_uXsrQ9NSMOd40PsiLaFf8ySjC3lKe5CKaN6CFeteg3I1A8ocbiOY5fekeiD64Ky2ePq5GweNpbKLtwEY38QznUeZ5Mp67CcRYI2K7jU-MU0M0cNdJ757gYP-r9plo_QdGwCkm7gXVsXaRYafTFVneJqaePgBE8junn7VTn58Ozaj7aYvdXvUvvO4qAVVOUOwF88QldAPS_hW_ykTKKx0oOlUnV16xradb_LZ05m09r9mgb9p7gGWyrCKZtmnhHFEgRjBS7_jcqAvizeCAx8iqLMJeVIDG1C9hKrFDwRDa-R2LojQECcxY0z04DYqfLn3Y2n2ntpdshmd8XuL4YHfWfzGfs7geepQLD8ZsOavDErSuO6jrehtXlu_xh8zbN2LwQxknKlhnBuMKC9b6SwRlVKaewNsSU8E293IRud6WIzz4RrUoWNRJA7digzKuSLNeeiX5Qr1IoXGOj2N1fc4DWGow-id-jMu-Tcct1N76OLx6GSGZwhUU_g8eYyTPG-sZEcY-GgOaXjBbK5BlNaM2ziLsz3GPP12GIQz2ojGcxv-fqBgqkCnGJJKpqN_csnC0zsuqulj5cVF_iz7SLPFGlT7TtyASdT6p2xK9H2ljINj9E=s0-d-e1-ft#http://maps.googleapis.com/maps/api/staticmap?size=298x298&amp;maptype=roadmap&amp;markers=icon%3Ahttp%3A%2F%2Fs3-ap-southeast-1.amazonaws.com%2Folacabsimages%2Finvoice%2FStart2x.png%7C28.613529400000%2C77.354994500000&amp;markers=icon%3Ahttp%3A%2F%2Fs3-ap-southeast-1.amazonaws.com%2Folacabsimages%2Finvoice%2FEnd2x.png%7C28.690099300000%2C77.374153600000&amp;path=weight%3A5%7Ccolor%3A0x4379ai9%7Cenc%3AqqsmDukcwMgVAqc%40IsWQy_%40XDv%5E_QjAoYf%40gYlC%7BNmBeLrTgTpWMLgGkH%7BHwNoZam%40aQc_%40y%5Cgs%40eGsOe%40mAsKoXqJoVef%40qXwBjI%7DGxAmLnJc%5DvOiH%7CAkGbA"
	hindon_to_office_map = "https://ci4.googleusercontent.com/proxy/prBck4ljSja9BbtQpnxrW7eXXj4kKiA576w57QQcpZEMpRb0x_VtV_KcrVBO_NINHhqc0hpdToWfp4NVsd660uLAwk1WrbNaT-8lD3O7_XRMgqSy8OFDBuulfr-vAyqFJWGxu8DCJFVdU8ML5GiW7-QoYtlO3QeioUdUzYMRtnpYzhbh_bgd3G7xyHFnapov60FMG9yYARCpE6ibSq65-YbG2RnjhXlfW-xmeFAq1gT98nF9FuduNey-yXVohqIyanEs_-acLBAr6-FOOjBUeMEHegwHkIMrl13zi5KNlT92FimWQX3ouZ2dkKqV_DFtIwa3fctGsN_6IrvtbKFRdUhk2mQOTWksEqrFuXUaXekX4Ez-Qbi2lGlIaQeu9s9jVSgdykP5OEtelgcmoo3rLhfB89Lgv57Nb10vMQoXcrbdwmrLE_rFu3qU0KsUKLv8yb67b8Y6Ndz2PZ0z1Ov6SDbhcgNOuRs8CngEjr75OXyymEsdpDkJU8Wqpi-WGjhOMq-1TDEbjGnLeKN8HFsUDggwXq5NOYQA0hgJ0qOv2ejWmHRgjbStEoh1kENV_rU9F3K9gDtULAM4X0pR2-v6CTEGUa3T3n508yTvwlnDquXwBNTh84sAA0EsOdJR3vNK72xRmsAfVVcWmpDPW0GBvV7pQX_KYxKHdRditg1j693coFw2OVWYGgZwp47ac40a4nhPlNZSTya5p4IVJDSKXBton6iJSaP_sLvWdg=s0-d-e1-ft#http://maps.googleapis.com/maps/api/staticmap?size=298x298&amp;maptype=roadmap&amp;markers=icon%3Ahttp%3A%2F%2Fs3-ap-southeast-1.amazonaws.com%2Folacabsimages%2Finvoice%2FStart2x.png%7C28.684818100000%2C77.376334100000&amp;markers=icon%3Ahttp%3A%2F%2Fs3-ap-southeast-1.amazonaws.com%2Folacabsimages%2Finvoice%2FEnd2x.png%7C28.615198000000%2C77.355060900000&amp;path=weight%3A5%7Ccolor%3A0x4379ai9%7Cenc%3AcoanDaqgwMda%40gZhCeJn%40kMpBdR%7C%5ExQvRvb%40zQnKrViM%7CRyJlO_FnKmBhNgBpSwIvQl%40rS%40tTX%60Yt%40lQXd%40pKCbPO%7EbAAre%40%7CRjFf%60%40N%60YNfZN"


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
	office_to_hindon = True  # Set True or False
	image_map = hindon_to_office_map
	driver_image="http://www.sagennext.com/wp-content/uploads/2009/10/Passport-Vijay1.jpg"


	if from_location is None and to_location is None:
		if office_to_hindon:
			from_location = "56a, Bishanpura Main Rd, Khora Colony, Sector 62, Noida"
			to_location = "Unnamed Road, Hindon Air Force Station, Hindon Residential Area, Ghaziabad"
			image_map = office_to_hindon_map
		else:
			to_location = "56a, Bishanpura Main Rd, Khora Colony, Sector 62, Noida"
			from_location = "Unnamed Road, Hindon Air Force Station, Hindon Residential Area, Ghaziabad"
			image_map = hindon_to_office_map


	# Contents with no editing required

	base_fare = base_fare + round(random.uniform(1,25),2)
	tax_rate = 7.6
	taxes = round((tax_rate * base_fare)/100.0,2)

	total_amount = int(base_fare + taxes)

	data = {
		"driver_image": driver_image,
		"driver_name": driver_name,
		"travel_date": travel_date,
		"from_time": from_time,
		"to_time": to_time,
		"from_location": from_location,
		"to_location": to_location,
		"base_fare": base_fare,
		"taxes": taxes,
		"image_map": image_map,
		"total_amount": total_amount,
		"order_id": order_id,
		"car_name": car_name,
	}
	return render(request, 'bills/ola.html', data)


def map_from_delhi(request):
	with open('/Userstatic/from_delhi', "rb") as f:
		return HttpResponse(f.read(), content_type="image/jpeg")
