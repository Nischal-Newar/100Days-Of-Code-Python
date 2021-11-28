#### Travel Log Program  ####
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# function to add a new record in travel_log 
def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
