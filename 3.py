arr = [1, 2, 7, 5, 7, 4, 1, 1, 2, 5]
res=[]
for i in range(len(arr)):
    for j in arr[i+1:]:
        if arr[i]>j:
            res.append((arr[i],j))
print(res)


           