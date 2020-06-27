squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) #0

print(max(digits)) #9

print(sum(digits)) #45

squares = [value ** 2 for value in range(1, 11)]
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]