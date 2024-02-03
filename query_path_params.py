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

print(query_average())
print(compute_avg_risk_params("Pittsburgh", "New York", dataset, filters))
print(compute_avg_risk_params("Chicago", "Los Angeles", dataset, filters))
print(compute_avg_risk_params("Boston", "Miami", dataset, filters))
