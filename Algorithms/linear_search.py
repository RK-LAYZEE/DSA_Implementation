def linear_search(query, target):
    for i in range(len(query)):
        if query[i] == target:
            return i
    return None

def verify(result):
    if result is not None:
        print(f"The target index is: {result}")
    else:
        print("The target index does not exist in the query")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prompt = int(input("Enter target value: "))
result = linear_search(data, prompt)
verify(result)