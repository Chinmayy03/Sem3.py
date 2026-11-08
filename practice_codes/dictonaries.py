countries={
    "India": "New Delhi",
    "USA": "Washington D.C.",
    "Japan": "Tokyo",
}
countries.update({"Germany": "Berlin"})

print(countries.get("Germany"))
countries.pop("USA")

print(countries)