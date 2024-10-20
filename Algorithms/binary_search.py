def binary_search(query, target):
    first = 0
    last = len(query) - 1 
    while first <= last:
        midpoint = (first + last) // 2
        
        if query[midpoint] == target:
            return (midpoint)
        elif query[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

def verify(result):
    if result is not None:
        print(f"The target index is: {result}")
    else:
        print("The target index does not exist in the query")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prompt = int(input("Enter target value: "))
result = binary_search(data, prompt)
verify(result)