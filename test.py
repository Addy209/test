class myds:
    def __init__(self,key,val):
        self.key=key
        self.value=val
        self.min_arr=[]
    
    def setMin(self,val):
        self.min_arr.append(val)
    
    def destroy_val(self, index):
        self.value[index]=None
    

t_case=1#int(input("Test Cases:"))
arr_size=7#int(input("Array Size:"))
arr=[7,3,2,4,9,12,56]

# print("Enter array:")
# for i in range(arr_size):
#     arr.append(int(input()))

children=5#int(input("Children Count:"))

diff=[]
for i in arr:
    row_diff=[]
    for j in arr:
        row_diff.append(i-j if i-j>0 else j-i)
    
    diff.append(row_diff)


obj_arr=[]
for i in range(arr_size):
    obj_arr.append(myds(arr[i],diff[i]))

for obj in obj_arr:
    for x in range(children-1):
        mini=99999999;
        min_index=None
        arr_loop=obj.value
        for i in range(len(arr)):
            if arr_loop[i]==0 or arr_loop[i]==None:
                continue
            if arr_loop[i]<mini and arr[i]>=obj.key:
                mini=arr_loop[i]
                min_index=i
        
        if min_index==None:
            continue
        obj.setMin(arr[min_index])
        obj.destroy_val(min_index)

min_diff=[]
for obj in obj_arr:
    arr_loop=obj.min_arr
    max_val=None
    if arr_loop:
        max_val=max(arr_loop)
        key=obj.key
        min_diff.append(max_val-key)

print(min(min_diff))