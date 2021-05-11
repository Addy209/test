arr=[7,3,2,4,9,12,56]
arr.sort()
children=5

def calculate_min():
    sub_arr=[]
    size=len(arr)
    for i in range(size):
        if i+children>=size:
            break
        sub_arr.append(max(arr[i:i+children])-min(arr[i:i+children]))

    print(min(sub_arr))
    
    
calculate_min()
