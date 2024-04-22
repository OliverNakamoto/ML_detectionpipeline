import matplotlib.pyplot as plt

# Function to extract points from the text file
def extract_points(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('Timestamp'):
                continue
            elif line.startswith('x'):
                continue
            elif line.strip():  # Non-empty line
                x, y, int= map(float, line.strip().split(','))
                points.append((x, y))
    return points

# Function to plot the points
def plot_points(points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    plt.scatter(x_values, y_values, s=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Point Cloud')
    plt.grid(True)
    plt.axis('equal')  # Set equal aspect ratio for the plot
    plt.show()

# Main function
def main():
    filename = "trial_2.3/1712591249.163667.txt"
    points = extract_points(filename)
    plot_points(points)

if __name__ == "__main__":
    main()
