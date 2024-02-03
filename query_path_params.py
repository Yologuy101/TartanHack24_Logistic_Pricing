from pathrisk import compute_avg_risk_params
from pathrisk import PathRisk
import numpy as np
import pandas as pd
import warnings 
warnings.filterwarnings("ignore")

dataset = pd.read_csv("US_Accidents_March23.csv")
filters = ["Severity", "Start_Time", "End_Time", "Distance(mi)", "State", "Start_Lat", "Start_Lng"]

def query_average():
    p1 = PathRisk(dataset, filters, "Pittsburgh", "New York")
    p1.time_difference_in_minutes()
    p1.convert_time_column_to_minutes()
    p1.compute_average_duration()
    print("The average parameters across the USA that assess the risk of travelling along a path:")
    return {"average crash severity":p1.average_severity, "average crash distance":p1.average_distance,
            "average number of accidents per year": p1.average_num_accidents_per_year, "average crash duration": p1.average_duration}

def compute_risk_factor(us_avg, path_avg):
    us_avg_severity = us_avg["average crash severity"]
    us_avg_crash_distance = us_avg["average crash distance"]
    us_avg_num_acc_year = us_avg["average number of accidents per year"]
    us_avg_crash_duration = us_avg["average crash duration"]

    weighted_avg = 0.2 * (path_avg[0] / us_avg_severity) + 0.3*(path_avg[1] / us_avg_crash_distance) + 0.3*(path_avg[2] / us_avg_num_acc_year) + 0.2*(path_avg[3] / us_avg_crash_duration)
    percent_increase = (weighted_avg - 1) / 10
    return percent_increase + 1

#USAGE:
"""us_avg = query_average()
path_avg = compute_avg_risk_params("Pittsburgh", "New York", dataset, filters)
compute_risk_factor(us_avg, path_avg)"""



#just examples
"""
#example 1
path_avg = compute_avg_risk_params("Pittsburgh", "New York", dataset, filters)
print(us_avg)
print(path_avg)
print(compute_risk_factor(us_avg, path_avg))

#example 2
path_avg = compute_avg_risk_params("Pittsburgh", "Miami", dataset, filters)
print(us_avg)
print(path_avg)
print(compute_risk_factor(us_avg, path_avg))

#example 3
path_avg = compute_avg_risk_params("Pittsburgh", "Los Angeles", dataset, filters)
print(us_avg)
print(path_avg)
print(compute_risk_factor(us_avg, path_avg))

#example 4
path_avg = compute_avg_risk_params("Pittsburgh", "Seattle", dataset, filters)
print(us_avg)
print(path_avg)
print(compute_risk_factor(us_avg, path_avg))

#example 5
path_avg = compute_avg_risk_params("Pittsburgh", "Oklahoma City", dataset, filters)
print(us_avg)
print(path_avg)
print(compute_risk_factor(us_avg, path_avg))

#example 6
path_avg = compute_avg_risk_params("Pittsburgh", "Houston", dataset, filters)
print(us_avg)
print(path_avg)
print(compute_risk_factor(us_avg, path_avg))

#example 6
path_avg = compute_avg_risk_params("Pittsburgh", "Houston", dataset, filters)
print(us_avg)
print(path_avg)
print(compute_risk_factor(us_avg, path_avg))

#more examples
cities = cities = [("Pittsburgh", "Houston"), ("New York", "Los Angeles"), ("Chicago", "Miami"),
          ("Denver", "Seattle"), ("Atlanta", "San Francisco"), ("Boston", "Dallas"),
          ("Philadelphia", "Phoenix"), ("Detroit", "San Diego"), ("Minneapolis", "Tampa"),
          ("St. Louis", "Portland"), ("Cleveland", "Charlotte"), ("Orlando", "Indianapolis"),
          ("Columbus", "Austin"), ("Salt Lake City", "Nashville"), ("Cincinnati", "Las Vegas"),
          ("Raleigh", "Hartford"), ("Kansas City", "Riverside"), ("Milwaukee", "Baltimore"),
          ("Sacramento", "Jacksonville"), ("Pittsburgh", "Houston"), ("New York", "Los Angeles"),
          ("Chicago", "Miami"), ("Denver", "Seattle"), ("Atlanta", "San Francisco"),
          ("Boston", "Dallas"), ("Philadelphia", "Phoenix"), ("Detroit", "San Diego"),
          ("Minneapolis", "Tampa"), ("St. Louis", "Portland"), ("Cleveland", "Charlotte"),
          ("Orlando", "Indianapolis"), ("Columbus", "Austin"), ("Salt Lake City", "Nashville"),
          ("Cincinnati", "Las Vegas"), ("Raleigh", "Hartford"), ("Kansas City", "Riverside"),
          ("Milwaukee", "Baltimore"), ("Sacramento", "Jacksonville"), ("Pittsburgh", "Houston"),
          ("New York", "Los Angeles"), ("Chicago", "Miami"), ("Denver", "Seattle"),
          ("Atlanta", "San Francisco"), ("Boston", "Dallas")]

for c1, c2 in cities:
    path_avg = compute_avg_risk_params(c1, c2, dataset, filters)
    print(us_avg)
    print(path_avg)
    print(compute_risk_factor(us_avg, path_avg))"""
