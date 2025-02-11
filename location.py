#a code to return the country and specific coodinate where the user is located
import requests

def get_location():
    try:
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        if data['status'] == 'success':
            return data['country'], (data['lat'], data['lon'])
        else:
            return None, None
    except requests.RequestException as e:
        print(f"Error fetching location data: {e}")
        return None, None
    

#call the function to get the location
if __name__ == "__main__":
    country, coordinates = get_location()
    print(f"Country: {country}, Coordinates: {coordinates}")