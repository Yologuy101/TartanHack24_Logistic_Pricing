from datetime import datetime
import googlemaps, polyline



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
        self.gmaps = googlemaps.Client(key="AIzaSyBU3qvC9Bl_6wIffZ4jd0NFd1Xj3ry81pY")
        self.directions = self.gmaps.directions(self.origin, self.destination, mode="driving", departure_time=self. start_time, traffic_model=self.traffic)

        self.gps, self.time_traffic, self.distance = self.get_info()
        # point along the path heuristic
        ratio = len(self.gps) / self.distance
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
