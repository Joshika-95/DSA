def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)
        
        # Fill in the middle values
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        triangle.append(row)
    
    return triangle

# Example usage
n = 5
triangle = generate_pascals_triangle(n)

# Print the triangle row by row
for row in triangle:
    print(row)