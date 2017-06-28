from random import randint

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def ola_bill(request):
	# Content to be edited
	driver_name = "Anas"
	travel_date = "20 March, 2017"
	distance = 14.6
	travel_time = 52
	from_time = "10:01 AM"
	to_time = "10:53 AM"
	from_location = "149, Ring Rd, Phase 1, Kilokri, Maharani Bagh, Sunlight Colony, New Delhi, Delhi 110014, India "
	to_location = "57, JSS Boys Hostel Rd, Khora Colony, Sector 62A, Ghaziabad, Uttar Pradesh 201301, India "
	driver_image ="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAF4ASQMBIgACEQEDEQH/xAAbAAACAgMBAAAAAAAAAAAAAAAABQEGAgMEB//EADcQAAEDAgQCBwYEBwAAAAAAAAEAAgMEEQUSITFBUQYTFHGBkcEiIzJhodFicrHwFUJSVJKi4f/EABoBAAMBAQEBAAAAAAAAAAAAAAAEBQMCAQb/xAAhEQACAgEEAgMAAAAAAAAAAAAAAQIRAwQSITFBUQUTFP/aAAwDAQACEQMRAD8AcoQhNEQCkOJ9JIKd74aRvXytGrh8De88Vh0wrZYaRtPA/IZQS917ENHAd/oqtSBrspip5bm+Vxbp5/vdZTyU6Q3g0+9bpDSo6R4oAX5qaNl7aMJt8uKzo+mEjHBtfAx7b6yQXFvA/daTAWnIYAXAAgBn6bJbidFUOs91OBfWwadFn9jXkb/NBqtp6JTVEVTCyaneHxvFw4cVvXnnRbFH4biAppswp5iGkHZh4H0P/F6EFvCSkrJ2bE8cqZKEIXRkCEIQBTelUfXY5DHIA5nVsyg8y4q94DE1kDBlDQABlA2Veq6Prsbp6pzbgROa0fia7f8A2TKjqa6F2SJ15DIGkGAlgPzN9B89lNzSUp8H0Glg8eNWWjJHbUDyXLXRxvhc1zA4HmLqKaulfCTVRxiRjbnLsUtxDFKtrg10cMUbr5CWOcdBc7DRYrkbfCspHSqihir4WNaIw/YsaAQQriL6X34pBjEEteKSQsBkbUNy5To5vH6J+PaAPA6p/TNVRG+RT3JkoQhMk0EIQgDANyva5zQbE2dxHE+nkn1O2J8efK0aakhInbIlqawMZFSFo3LnO4BTM2PbM+h0mdZMV+uBrHGZDUOtYFt9eS3U8MctOBINhqClDMKdNG+U1T2ukHt5ZWi/hZaqarraV3ZpGh8IGVkmlzbnZZbRtyOitydsZkBsy9rd1vVaRoAoBLpXOusk9pYNLc/JF+RzKUlBeAQhCaJoIQASQACSdABxTig6OV9VYyM7PGeMm/8Ajv52Xjkl2dRhKbqKFtHSvrKhkEY1dueQ4lcjSYnNe8XYQvQMKwaDDi90Zc+QjKXu5Ku4vhzIKuentZpPWRflPDwNx5JPUSumWdHh+uLT7Yq7ZR3B6ppPMnVc7pOvf7kGw1PILqGGRk2MZ/NnNvK67oKG7Y6aAASyuytNtjz8Bc+CWteBzb7FYZkazjmaHX53APqhXqXAqF1HDTviNoImxMeDZwAFhqlFZ0TqGAvopWzN4Nf7LvsfoqMJqqImfTT3OS5RXELdVUlTSOy1MEkZ4Zm6HuPFaVqJtNdnpGHYVSYewCniAfbWR2rj4rsI1WSg7hKstpJcI5ppRAx78rnncMYLl3ckGLR1WIUAqX0zaeppnZmMz5i5n8wOnLXwCtFhyWuSFrtdiuWrVGkZJMpAiv7QLbb7rtwKGXrJ8QazrCxpjp2E5Q48T+gv3qcUwCc19OyjI7LM739re60vcfI7fI/SzQU7GMaxjcrGDK1o5LHHiads3nlTRw0WIPnPVVlJLTy6C/xMcTyI9UyaNcp4BZBoGyyW4u2n0YSQxyxmORjXsO7XC4KXfwDC/wCyj8z900WOZe3Rw4p9oyQoClB6ShCCgDSxodI5x52W5Yxj2fFSEAyVCEFABzXPn/Ct4PxJP2qT+hnmg7irP//Z"
	car_name = "Micro - White hyundai i10"
	order_id = "CRN614998301"
	# Content till when edited allowed




	from_noida = False
	map_image = "https://ci5.googleusercontent.com/proxy/zTCUvn2Yz7x-oQ-RrbMCPWJ22R0WQkE4jXIaL9lhPtn09Fz-EVDOiWFl8DAtPmFMVETOOdDZ3i174kb3bbWAyqiprYbB-8NXyRRJ98xVm80To9eDIYg3mqqnD129QawsOK_Uqin-l7l1DiFwiFWyx7OTTpR3kdrvjQ-HXxQyVSDGMQTK0Vh9JxtH18eCBL0xZUyorQANec7GJ4iGSjD5uR8iByk5mMpOYRPmrku7Z-uDtgV0477K5OcpqbmBbx9P5VmvQIBBU_CyfKZg88V-7DflaVxH9ENDNKLc0gHJaobN8gqwbSmSUXDe6X4vjGlj_OjqUkdTUZLkDiYEx8Xhinem2K-3N6_KdxPQmb6UprjWZEYRETHOTvpQTQau5rYfeXj3Z7Zvb5j7cwKZ3Wx_DGVwlbWMlmCdol_fxQ0xXTN9UWtShSSla2yACrstMOCWWXEn84pQH4V1VtUutBbh_ygsccdLaoRfY7oJGOCdMDjX34x1uwobeNN37YpyKgYtxgY7Nx-LRZOBNCePDLh6zwduSFe5KY2-0rfSABz_kg-x0D-dnGAzRFGCYYS2c6zGS-t-DaXY4Qx51_Gdprgj3GlJegrpFzh-0mGxa7T1k984kJ8v313td55box6n1g3aAW2fMKUcjoz6Sb4HRiHC62dDM-NaC8OqdujNj2Vt8yIzHzBa_E2785yxpuZIJn-zPfb2KAlqq4XtH-WIaQ=s0-d-e1-ft#http://maps.googleapis.com/maps/api/staticmap?size=298x298&amp;maptype=roadmap&amp;markers=icon%3Ahttp%3A%2F%2Fs3-ap-southeast-1.amazonaws.com%2Folacabsimages%2Finvoice%2FStart2x.png%7C28.575965000000%2C77.263211700000&amp;markers=icon%3Ahttp%3A%2F%2Fs3-ap-southeast-1.amazonaws.com%2Folacabsimages%2Finvoice%2FEnd2x.png%7C28.614613300000%2C77.354966700000&amp;path=weight%3A5%7Ccolor%3A0x4379ai9%7Cenc%3AyflmDanqvMiRsZ%7EC%7B%7C%40tEsaA%7BL%7BnEcAkAsAiBmP_WyLaRuLwPiQmX%3F%3F%3F%3FqOmUwFgIm%5BqPyA%7D%40mUaEw%5BrCcHiUmDy%5BgE%7BFmWwC"
	if 'delhi' in to_location.lower():
		from_noida = True
		map_image = "https://ci4.googleusercontent.com/proxy/B6NMpNiWHa0-fdC1LwQb0Pfbx16P6BNnDolQK2Hgr_jFxzK_m1u6OHrOQV7PKZxYAPncELrcqLk2kfWad6J3UgL7G7xs6hc26v2Hl40bKwkU-Sz1wCCZK0iiLPR4V9ot6QWEAWIf6SGBpOM5OKbI6Vwe9SmSXzx8U7DOyBqzyAsvUactW0HnH36RZ9TOqj3beTfLu0OgUpVPPtWuPDGDn4_AnxxeCf8R6qYwZLhX41y_WPrtqfPJhs1IviBRiZGbZOtzvaZJ7ZeM83LLOMll69NlC2IhXoSIvPxiYx3NoLc3lm8W7dfw9KjVpVnn16n_zPdMkDq03kpM-D1ChBKRseYtCYWD_TlyUw5kAG5w1YBxHD-JPFf_Ruav7mvcz5JpKfJfTQ5ojuhA7Eik9qRdS99Hh7rrXPlQRg1GQ_nSBbJAarI1BwAP26OnPEoabruZXrT84GTiUMtkah1chBoz1ZIYTiPxSAJnW7JCRozNZPK3pk_em1YoELEwvHMm-GUeteey7OdtYTHEXp5u4S4WiulkfAuYXICH5BQ5E_6111rhZL1BkwWLzdoQKwpm11YeQz_xNyzjaw58lgU2OLMMsp_0vGo2TgK3nfQ36MO7Er4oJrEkxKwfDD02thOMlvj9mABXdPXLUluca2oawglpoLCDYfvVclRd5-7t_0sN_lFMCQMc0LbcvhhNxPTs-ugZMwFaSbG3h0l-wV063q6qMciV-7bMIUsf6Q_oFxbSEC87Qo7WEi4mScgghq46rTxG5YYVwa8Otdl1hiXV32lMJ_Favsi6aWakOB-SowhHTL15FBXsTKAIicSCDQAg3fvt2Gux4lgldIQeu2Rpze7LrnHzJY7R83Y-oMHMRbSgtKJHhEtYr06O77SWt6aPyEaa3WlFQcT2m96PgMP8g3LsNhhuEjbH3EZP9wlf1rgA1KSwrPn-GWaB2Xtaygr9BE0QN91N_5nhaGcJp7qhUKsiRvevd4YzY52G10w4MLGCpQ6oFTmJujVdVH3qpohG3QkEy4Z1nbZ6ugzTHhx8F12hu47pew-S78DHORpoGmMdEqs3WuKglKOYjl5BGgsYTijKtduCFU5HKmtyjQ_CtmNwaekeffgIUwM0u2SJlxM6pIUI=s0-d-e1-ft#http://maps.googleapis.com/maps/api/staticmap?size=298x298&amp;maptype=roadmap&amp;markers=icon%3Ahttp%3A%2F%2Fs3-ap-southeast-1.amazonaws.com%2Folacabsimages%2Finvoice%2FStart2x.png%7C28.611961000000%2C77.354649300000&amp;markers=icon%3Ahttp%3A%2F%2Fs3-ap-southeast-1.amazonaws.com%2Folacabsimages%2Finvoice%2FEnd2x.png%7C28.570899100000%2C77.266785500000&amp;path=weight%3A5%7Ccolor%3A0x4379ai9%7Cenc%3AwgsmDqicwMdHbAbEvHnClNfVaB%7CZkC%3F%3FtChFfAlONrBNbBVdEX%7ECbHfA%60NrIdGlHrDxF%7CMlR%3F%3FfPvVxQrXvFfIbEhGDFX%60%40%3F%3FC%3FDDdBlCtA%7CBEMBN%40FAAFSvD%60GhIjMzVn_%40lPzo%40wd%40je%40eExr%40vEjNrAzD%7EAvEt%40dC%7CAbFrAtDl%40fCLv%40Hv%40PfADvADnADtAWdGKpBMj%40iBpHo%40lAgAhBk%40v%40iBzBoCfDwBhCcCvC%7BC%60EmCvQT%60C%5EzAh%40fBl%40hAp%40tA%60AdAr%40%7C%40%60AhAbApAdAdA%7CAfBzCnDzBpD%7CBvDP%5E%60En%40%7ELuJpAk%40v%40%5Bt%40OnB_A%7EA%7D%40"

	state_tax = True
	# if not from_noida:  # if start trip from delhi
	# 	state_tax = False
	# x = from_location
	# from_location = to_location
	# to_location = "Mindfire solutions, Noida, Uttar Pradesh"

	base_fare = 40
	km_charge = 6
	distance_fare = km_charge * distance
	total_base_fare = base_fare + distance_fare + travel_time
	taxes = round((10.71 * total_base_fare) / 100.0, 1)
	total_amount = int(taxes + total_base_fare + (100 if state_tax else 0))
	# order_id = "CRN" + randint(590000000, 799999999).__str__()

	data = {
		"driver_name": driver_name,
		"travel_date": travel_date,
		"travel_time": travel_time,
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
		"driver_image": driver_image,
		"map_image": map_image
	}
	return render(request, 'bills/ola.html', data)


def map_from_delhi(request):
	with open('/Userstatic/from_delhi', "rb") as f:
		return HttpResponse(f.read(), content_type="image/jpeg")
