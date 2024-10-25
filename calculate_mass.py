import csv
import numpy as np
import matplotlib.pyplot as plt

file_name="satellite_mass_database_1.csv"

def calculate_mass():
    x_values=list()
    y_values=list()
    with open(file_name, "r") as csv_file: 
        reader=csv.reader(csv_file, delimiter=",")
        for row_line in reader:
            if row_line[0]!= "project":
                payload_mass=float(row_line[6])
                wet_mass=float(row_line[7])
                calculated_value=payload_mass/wet_mass
                x_values.append(payload_mass)
                y_values.append(calculated_value)
        return x_values,y_values 

def generate_chart(payload_mass_list, wet_mass_list): 
    fig = plt.figure(figsize = (10, 5))
    plt.bar(payload_mass_list, wet_mass_list, color ='blue',
            width = 0.1)
    
    plt.xlabel("payload mass")
    plt.ylabel("wet mass")
    plt.title("Payload Mass vs. Total Satellite Mass")
    plt.show()

x_values,y_values=calculate_mass()
generate_chart(x_values,y_values)




