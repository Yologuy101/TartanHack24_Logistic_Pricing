from datetime import datetime
import googlemaps, polyline, requests
import time



class RouteInfo():

    """
    route = get_gps_location.RouteInfo(s, e)
    then route.gps
    """

    def __init__(self, origin, destination, start_time=datetime.now(), traffic='pessimistic'):
        self.origin = origin
        self.destination = destination
        self. start_time = start_time
        self.traffic = traffic
        self.key = "AIzaSyBU3qvC9Bl_6wIffZ4jd0NFd1Xj3ry81pY"
        self.gmaps = googlemaps.Client(key=self.key)
        self.directions = self.gmaps.directions(self.origin, self.destination, mode="driving", departure_time=self.start_time, traffic_model=self.traffic)

        self.gps, self.time_traffic, self.d1 = self.get_info()

        res = list(filter(lambda x: x.isdigit(), self.time_traffic.split()))
 
        # use a list comprehension to convert the remaining elements to integers
        res = [int(s) for s in res]
        
        if len(res) == 3:
            self.time_traffic_d = res[0]
            self.time_traffic_h = res[1]
            self.time_traffic_m = res[2]

        elif len(res) == 2 and 'day' in self.time_traffic and 'hour' in self.time_traffic:
            self.time_traffic_d = res[0]
            self.time_traffic_h = res[1]
            self.time_traffic_m = 0
        elif len(res) == 2 and 'day' in self.time_traffic and 'minute' in self.time_traffic:
            self.time_traffic_d = res[0]
            self.time_traffic_h = 0
            self.time_traffic_m = [1]
        elif len(res) == 2 and 'hour' in self.time_traffic and 'minute' in self.time_traffic:
            self.time_traffic_d = 0
            self.time_traffic_h = res[0]
            self.time_traffic_m = res[1]
        elif len(res) == 1 and 'minute' in self.time_traffic:
            self.time_traffic_d = 0
            self.time_traffic_h = 0
            self.time_traffic_m = res[0]
        elif len(res) == 1 and 'hour' in self.time_traffic:
            self.time_traffic_d = 0
            self.time_traffic_h = res[0]
            self.time_traffic_m = 0
        elif len(res) == 1 and 'day' in self.time_traffic:
            self.time_traffic_d = res[0]
            self.time_traffic_h = 0
            self.time_traffic_m = 0



        # self.time_traffic_m = float(self.time_traffic[self.time_traffic.find('s ')+2:self.time_traffic.find('s ')+4])
        self.distance = int(self.d1['text'][:self.d1['text'].find(' ')].replace(',', ''))
        # point along the path heuristic
        ratio = len(self.gps) / int(self.d1['text'][:self.d1['text'].find(' ')].replace(',', ''))
       
        k = 0.2/ratio
        step = int(1/k)
        self.reduce_gps = self.gps[::step]
        
        

    def get_info(self):

        """
        returns the gps info
        """

        poly = []

        # Extract road names
        if self.directions:
            route = self.directions[0]['legs'][0]
            steps = route['steps']
            for step in steps:
                p = step['polyline']['points']
                poly.append(p)

            time_traffic = route['duration_in_traffic']['text']
            distance = route['distance']

        else:
            print("No directions found.")

        coord = []
        for l in poly:
            temp = polyline.decode(l, 5)
            for pair in temp:
                coord.append(pair)

        return coord, time_traffic, distance
    
    def get_address(self):

        result = set()
        # s = []
        c = self.reduce_gps[::20] 
        for coord in c:
            lat = coord[0]
            lon = coord[1]
            # print(lat, lon)

            url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&result_type=administrative_area_level_1&key={self.key}"

            response = requests.get(url)
            data = response.json()
            
            # if 'results' in data and data['results']:
            result.add(data['results'][0]['address_components'][0]['short_name'])
            # s.append(data)

        
            # return "Address not found"

        return result
    
    def get_live_route_weather(self):

        step_count = int(float(len(self.gps))/((self.time_traffic_h)+self.time_traffic_d*24))
    
        path_weather = []

        weather_loc = self.gps[::step_count]
        # weather_loc.append(self.reduce_gps[-1])
        st = self.start_time
        st = self.datetime_from_local_to_utc(st)
        for lat, lon in weather_loc:
            # print(lat, lon)
            
            year = st.year
            month = st.month
            day = st.day
            hour = st.hour
            minute = st.minute
            st = datetime(year, month, day, hour, 0)
            
            if hour + 1 > 23:
                hour = (hour + 1) % 24
                day += 1
            else:
                hour = (hour + 1) % 24
            
            et = datetime(year, month, day, hour, 0)
           
            # print(st, et)
            
            payload = {
                "location": f"{lat}, {lon}",
                "fields": ["precipitationProbability", "precipitationType", "temperature", "windSpeed", "windDirection", "precipitationIntensity"],
                "units": "imperial",
                "timesteps": ["1h"],
                "startTime": f"{datetime.isoformat(st)}",
                "endTime": f"{datetime.isoformat(et)}"
            }
            headers = {
                "accept": "application/json",
                "Accept-Encoding": "gzip",
                "content-type": "application/json"
            }

            # st = self.datetime_from_utc_to_local(et)
        
            st = et
            
            url = "https://api.tomorrow.io/v4/timelines?apikey=Lu2ByVGmsKqlhWaoRt5N22UR07LbOjE4"
            response = requests.post(url, json=payload, headers=headers).json()

            path_weather.append(response)
        return path_weather, weather_loc


    def datetime_from_utc_to_local(self, utc_datetime):
        now_timestamp = time.time()
        offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
        return utc_datetime + offset

    def datetime_from_local_to_utc(self, utc_datetime):
        now_timestamp = time.time()
        offset = datetime.utcfromtimestamp(now_timestamp) - datetime.fromtimestamp(now_timestamp) 
        return utc_datetime + offset
        

    def get_city_weather(self):
        result = {}
        w, loc = self.get_live_route_weather()
        # w=[1,2,3]
        # loc = [(38.83408, -104.82075),
        #         (38.86098, -104.91272),
        #         (38.88996, -104.95847)]
        for l, c in zip(w, loc):
            lat = c[0]
            lon = c[1]
            # print(lat, lon)

            url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&result_type=administrative_area_level_2&key={self.key}"
            response = requests.get(url)
            data = response.json()
            
            # if 'results' in data and data['results']:
            r = data['results'][0]['address_components'][0]['short_name']
            result[r] = l
            # return "Address not found"['plus_code']['']

        return result