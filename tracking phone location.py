import phonenumbers
from phonenumbers import geocoder
phno1 = phonenumbers.parse("+918943111275")
phno2 = phonenumbers.parse("+971526259029")
phno3 = phonenumbers.parse("+12896714260")


print("\n Pnone number Location\n")
print(geocoder.description_for_number(phno1,"en"));
print(geocoder.description_for_number(phno2,"en"));
print(geocoder.description_for_number(phno3,"en"));