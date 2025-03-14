import requests
from opencage.geocoder import OpenCageGeocode

# Function to get the current location
def get_current_location(api_key):
    geocoder = OpenCageGeocode(api_key)
    result = geocoder.geocode("Plot No 43/A, 43/B, Rd Number 16B, Gopalnagar Society, Hafeezpet, Hyderabad, Telangana 500085, India")
   # return "17.488554445079483","78.3747876802529"
   #for index, value in enumerate   (result):
    #   print(index, value)
   # print(result)
    if result and len(result):
        return result[0]['geometry']['lat'], result[0]['geometry']['lng']
    else:
        raise Exception("Geocoding failed")

# Function to get nearby places
def get_nearby_places(api_key, location, place_type):
   # print(place_type)
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location[0]},{location[1]}&radius=1500&type={place_type}&key={api_key}"
   # print(url) 
    response = requests.get(url)
    return response.json()

# Main function
def main():
    google_api_key = "AIzaSyB-aUav8DSYUJPvKIFJvdjAYR6iyWNAJ1g"
    opencage_api_key = "4312606e87464e21be017bdd3876e69f"
    location = get_current_location(opencage_api_key)
    place_types = ["restaurant", "supermarket", "book_store", "grocery_or_supermarket", "beauty_salon", "shopping_mall"]

    for place_type in place_types:
        places = get_nearby_places(google_api_key, location, place_type)
        print(f"Nearby {place_type.replace('_', ' ').title()}s:")
        for place in places['results']:
            print(f"- {place['name']}")

if __name__ == "__main__":
    main()