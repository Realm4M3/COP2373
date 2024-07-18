import math
import random

def calculate_hypotenuse(nearest_angle_degrees, adjacent_side):
    # Convert angle from degrees to radians
    angle_radians = math.radians(nearest_angle_degrees)
    
    # Calculate the hypotenuse using trigonometry (cosine function)
    hypotenuse_length = adjacent_side / math.cos(angle_radians)
    
    return hypotenuse_length

def main():
    # Generate a random angle between 1 and 89 degrees
    nearest_angle_degrees = random.randint(1, 89)
    
    # Prompt the user to input the length of the adjacent side
    adjacent_side = float(input("Enter the length of the adjacent side: "))
    
    # Calculating the length of hypotenuse
    hypotenuse_length = calculate_hypotenuse(nearest_angle_degrees, adjacent_side)
    
    # Printing the results
    print(f"For an angle of {nearest_angle_degrees} degrees and an adjacent side length of {adjacent_side}:")
    print(f"The length of the hypotenuse is approximately {hypotenuse_length:.2f} long.")

if __name__ == "__main__":
    main()
