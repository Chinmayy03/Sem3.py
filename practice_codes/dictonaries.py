countries={
    "India":"New Delhi",
    "USA":"Washington DC",
    "UK":"London"
}
countries["China"]="xin chao"
countries["Japan"]="Tokyo"
your_country=input("Enter your country name: ")

if your_country in countries:
    print("The capital of ur country is:", countries.get(your_country))

else:
    print("Your country isnt in the list")

print(countries.get("India"))