import datetime
from zoneinfo import ZoneInfo
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

geolocator = Nominatim(user_agent="time_checker")
tf = TimezoneFinder()

def get_current_time(city: str) -> dict:
    try:
        location = geolocator.geocode(city)
        if not location:
            raise ValueError("City not found.")

        latitude = location.latitude
        longitude = location.longitude

        tz_identifier = tf.timezone_at(lat=latitude, lng=longitude)
        if not tz_identifier:
            raise ValueError("Timezone not found for location.")

        tz = ZoneInfo(tz_identifier)
        now = datetime.datetime.now(tz)
        report = (
            f'The current time in {city.title()} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
        )
        return {"status": "success", "report": report}

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Could not determine time for '{city}': {str(e)}"
        }
