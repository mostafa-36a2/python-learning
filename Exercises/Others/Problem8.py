def CountWords(s: str):
    res = s.split(" ")
    print(res)
    return len(res)


x = CountWords("Hello Here we are in this place")
print("Count of words is: ", x)
