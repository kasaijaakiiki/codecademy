destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
# test_traveler = Name, destination, interest Name, Tag Name
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#get destination Indexs
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  print("Des_index", destination_index)
  return destination_index

get_destination_index("Los Angeles, USA")
#get_destination_index("Hyderabad, India")

# get traveler Location
def get_traveler_location(traveler):
  #traveler_destination = test_traveler[traveler]
  traveler_destination = traveler[1]
  #print(traveler_destination)
  #return traveler_destination
  traveler_destination_index = get_destination_index(traveler_destination)
  #print(traveler_destination_index)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print("Destination_index, ", test_destination_index)
#get_traveler_location(0)

#attractions = [[], [], [], [], []]
attractions = []
for destination in destinations:
  attractions.append([])
print(attractions)

def add_attraction(destination, attraction): 
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index].append(attraction)
  return attractions_for_destination

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print('Add Attractions:', attractions)

# Adding more attractions with Tags
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print('Added Attractions:', attractions)


def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])
print("Found Interested Attraction:", la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = ("Hi ", traveler[0], "we think you'll like these places around", traveler_destination)
  for attra in range(len(traveler_attractions)):
    return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print("Traveler_attraction", smills_france)


