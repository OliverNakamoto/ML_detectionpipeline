import numpy as np
from scipy.optimize import minimize

# Define the corresponding points in the first coordinate system
#a_points = np.array([[x, 0] for x in range(1, 6)])  # Assuming points are along x-axis
a_points = np.array([[17.76445960998535, 14.106902122497559], [15.644609451293945, 15.843428611755371], [11.982672691345215, 17.70400619506836]]) #1712591249.1138918

# x:17.76445960998535 1
# y:14.10690212249755
# x:15.644609451293945 2
# y:15.843428611755371
# x:11.982672691345215 3
# y:17.70400619506836
# Define the corresponding points in the second coordinate system
#b_points = np.array([[x + 1, 1] for x in range(1, 6)])  #1712591252.165763    # Assuming translated and rotated
b_points = np.array([[17.491058349609375, 13.46243953704834], [15.454221725463867, 15.252721786499023], [11.821630477905273, 17.22370147705078]])
# x:17.491058349609375 1
# y:13.46243953704834
# x:15.454221725463867 2
# y:15.252721786499023
# x:11.821630477905273 3
# y:17.22370147705078
# Function to calculate residual errors
# def residual_errors(params, a_points, b_points):
#     # params contains 3 values: translation_x, translation_y, rotation_angle
#     translation_x, translation_y, rotation_angle = params
#     rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
#                                 [np.sin(rotation_angle), np.cos(rotation_angle)]])
    
#     # Apply translation and rotation to a_points
#     transformed_a_points = np.dot(rotation_matrix, a_points.T).T + np.array([translation_x, translation_y])
    
#     # Calculate residual errors (squared Euclidean distance)
#     errors = np.sum((transformed_a_points - b_points)**2, axis=1)
#     return errors

def residual_errors(params, a_points, b_points):
    # Reshape params into (translation_x, translation_y, rotation_angle)
    translation_x, translation_y, rotation_angle = params
    
    # Reshape a_points and b_points to (N, 2) arrays
    a_points = a_points.reshape(-1, 2)
    b_points = b_points.reshape(-1, 2)
    
    # Calculate rotation matrix
    rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                                [np.sin(rotation_angle), np.cos(rotation_angle)]])
    
    # Apply translation and rotation to a_points
    transformed_a_points = np.dot(rotation_matrix, a_points.T).T + np.array([translation_x, translation_y])
    
    # Calculate residual errors (squared Euclidean distance)
    errors = np.sum((transformed_a_points - b_points)**2)
    return errors


# Initial guess for parameters (translation_x, translation_y, rotation_angle)
initial_guess = np.array([0, 0, 0])

# Minimize the sum of squared errors
result = minimize(residual_errors, initial_guess, args=(a_points, b_points), method='Powell', tol=1e-20)

# Extract the optimal parameters
translation_x, translation_y, rotation_angle = result.x

# Print the results
print("Optimal Translation (x, y):", translation_x, translation_y)
print("Optimal Rotation Angle:", rotation_angle)
