import math
import pandas as pd
import numpy as np
from get_gps_location import RouteInfo

class PathRisk(RouteInfo):
    def __init__(self, dataset, filters, source, destination):
        self.dataset = dataset
        self.features = self.dataset[filters]
        self.total_highway_length = 164000
        self.average_severity = self.features["Severity"].sum() / self.features.shape[0]
        self.average_distance = self.features["Distance(mi)"].sum() / self.features.shape[0]
        self.average_num_accidents_per_year = self.features.shape[0] / self.total_highway_length
        self.average_duration = None
        self.source = source
        self.destination = destination 
        route = RouteInfo(self.source, self.destination)
        self.path = route.reduce_gps
        self.states = route.get_address()
        self.distance = int(route.distance)
        self.number_of_accidents_total = self.features.shape[0]

    def time_difference_in_minutes(self):
    
    # Use pd.to_datetime without specifying a format to automatically infer it
        self.features['Start_Time'] = pd.to_datetime(self.features['Start_Time'], errors='coerce')
        self.features['End_Time'] = pd.to_datetime(self.features['End_Time'], errors='coerce')
        
        # Calculate duration and add it as a new column
        self.features['Duration'] = self.features['End_Time'] - self.features['Start_Time']
    
        return self.features
    
    def compute_average_duration(self):
        counter = 0
        s = 0
        arr = self.features.values
        for i in range(arr.shape[0]):
            val = arr[i][arr.shape[1] - 1]
            if val <= 300:
                counter += 1
                s += val
        self.average_duration = s / counter
        return self.average_duration
    
    def convert_time_column_to_minutes(self, column_name='Duration'):
        # Convert the column to Timedelta
        self.features[column_name] = pd.to_timedelta(self.features[column_name])

        # Convert Timedelta to minutes and store in a new column
        self.features['Duration(min)'] = self.features[column_name].dt.total_seconds() / 60
        self.features.drop('Duration', axis=1, inplace=True)
        self.average_duration = self.features['Duration(min)'].mean()
        return self.features
    
    @staticmethod
    def haversine_distance(lat1, lon1, lat2, lon2):
    
        # Radius of the Earth in miles
        R = 3958.8

        # Convert latitude and longitude from decimal degrees to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        # Difference in coordinates
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad

        # Haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c

        return distance
    
    def filter_states_dataset(self):
        filtered_rows = self.features[self.features['State'].isin(self.states)]
        self.features = filtered_rows
        return self.features

    def sorted_array(self):
        arr = np.array(list(zip(self.features['Start_Lat'], self.features['Start_Lng'], self.features['Severity'],
                            self.features['Distance(mi)'], self.features['Duration(min)'])))
        sorted_indices = np.argsort(arr[:, 1])
        sorted_coordinates = arr[sorted_indices]
        return list(sorted_coordinates)

    def compute_coordinates_along_path(self, ls, dist = 1):
        
        arr = ls.copy()
        coords = []
        for point in self.path:
            x1 = point[1]
            y1 = point[0]
            i = 0
            counter = 0
            
            while len(arr) > i and (self.haversine_distance(0, x1, 0, arr[i][1]) < dist or counter == 0):
                #x reached in circle
                if self.haversine_distance(0, x1, 0, arr[i][1]) < dist:
                    counter += 1 # entered circle
                    
                    if self.haversine_distance(y1, x1, arr[i][0], arr[i][1]) < dist:
                        #coords.append((arr[i][1], arr[i][0]))
                        coords.append(arr[i])
                        
                            
                i += 1 
                
            arr = arr[i:]
            
        return coords
    
    def get_avg_coords(self):
        
        final_dataset = self.filter_states_dataset()
        final_dataset.reset_index(inplace = True, drop = True)
        coords = self.compute_coordinates_along_path(self.sorted_array())
        coords = np.array(coords)
        return coords
    
    def get_avg_params(self, coords):
        severity_filtered_avg = np.mean(coords[:, 2])
        distance_filtered_avg = np.mean(coords[:, 3])
        duration_filtered_avg = np.mean(coords[:, 4])
        num_acc_filtered_avg = coords.shape[0] / self.distance
        return severity_filtered_avg, distance_filtered_avg, duration_filtered_avg, num_acc_filtered_avg

#create objects

def compute_avg_risk_params(origin, destination, dataset, filters):
    path1 = PathRisk(dataset, filters, origin, destination)
    path1.time_difference_in_minutes()
    path1.convert_time_column_to_minutes()
    path1.filter_states_dataset()
    coords = path1.get_avg_coords()
    avg_coords = path1.get_avg_params(coords)
    print("Path: {0} to {1}: crash severity | crash distance | number of accidents per year | crash duration".format(origin, destination))
    return avg_coords



