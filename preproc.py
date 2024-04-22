import os
import pandas as pd
import matplotlib.pyplot as plt


# Function to extract first two float numbers from each line after 'cones:' string
def extract_floats(lines):
    result = []
    found_cones = False
    for line in lines:
        if found_cones:
            floats = [round(float(x), 5) for x in line.split(",")[:2]]
            result.append(floats)
        elif "x:" in line:
            found_cones = True
    return result

def extract_xs(lines):
    x_vals = []
    found_cones = False
    for line in lines:
        if found_cones:
            if 'x:' in line:
                x_vals.append(round(float(line.split(":")[-1].rstrip("\n")),5))
        elif 'cones' in line:
            found_cones = True
    return x_vals

# Directory path
directory = 'trial_3.1/raw_data'
dir2 = 'trial_3.1/label'

# List to store DataFrames for each file
dfs = []

# Iterate through each file in the directory

for filename in os.listdir(directory):
    if filename.endswith(".txt") and not filename.endswith("3667.txt"):
        print(filename)
        filepath = os.path.join(directory, filename)
        filepath2 = os.path.join(dir2, 'labels_'+filename)
        with open(filepath, 'r') as file:
            lines = file.readlines()
            floats = extract_floats(lines)
            df = pd.DataFrame(floats, columns=['x', 'y'])
            df['label'] = 0
        with open(filepath2, 'r') as file:
            lines = file.readlines()
            x_vals = extract_xs(lines)
        for i in range(len(df)):
            if df.iloc[i,0] in x_vals:
                print(i)
                df.iloc[i,2] = 1
        dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
final_df = pd.concat(dfs, ignore_index=True)

# Display the DataFrame
#print(final_df)


#plotting dataframes

def extract_points(df):
    points = []
    for i in range(len(df)):
        if df.iloc[i,2]==1:
            x, y = df.iloc[i,0], df.iloc[i,1]
            points.append((x,y))
    return points

# Function to plot the points
def plot_points(points, i):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    plt.scatter(x_values, y_values, s=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(i)
    plt.grid(True)
    plt.axis('equal')  # Set equal aspect ratio for the plot
    plt.show()

for i in range(len(dfs)):
    points = extract_points(dfs[i])
    plot_points(points, i)
    #print(i)
    #print(dfs[i])


