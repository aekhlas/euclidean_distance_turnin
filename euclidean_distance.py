# Euclidean Distance – Difficulty 2 (Integers)

# A class to store 2D Cartesian coordinates (integers only)
class Point:
    def __init__(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("For Difficulty 2, both coordinates must be integers.")
        self.x = x
        self.y = y


# square root using Newton's method
def sqrt_int(n):
    if n < 0:
        raise ValueError("Cannot take square root of a negative number for Difficulty 2.")

    if n == 0:
        return 0

    guess = n
    for _ in range(20):
        guess = (guess + n // guess) // 2
    return guess


# Calculate distance between two integer points
def distance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    squared = dx * dx + dy * dy
    return sqrt_int(squared)


# Example usage
if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(7, 14)

    print("Point 1:", p1.x, p1.y)
    print("Point 2:", p2.x, p2.y)
    print("Distance =", distance(p1, p2))
