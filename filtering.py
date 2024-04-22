# Define the input and output file paths
input_file = "trial_3.59/1708785083.278002.txt"

# Define the filtering criteria for x and y values
min_x = 0.5
max_y = 2.1
min_y = -2.1

# Open the input file for reading
with open(input_file, "r") as f:
    lines = f.readlines()  # Read all lines from the input file

# Initialize a list to store filtered points
filtered_points = []

# Iterate through each line in the input file
for line in lines:
    print(line)
    if ('x' in line) or ('T' in line):
        pass
    else:    
        # Split the line into x and y values (assuming they are separated by whitespace)
        lists = line.split()
        x = float(lists[0].strip(','))
        y = float(lists[1].strip(','))
        #x, y = map(float, line.strip(',').split())  # Assuming the format is "x y"
        # Check if the point satisfies the filtering criteria
        if min_x < x and min_y < y < max_y:
            filtered_points.append((x, y))  # Add the point to the filtered points list

# Write the filtered points to the output file
a,b = input_file.split('/')
output_file = f'filter.{b}'
with open(output_file, "w") as f:
    for point in filtered_points:
        f.write(f"{point[0]} {point[1]}\n")  # Write each point to a new line in the output file
