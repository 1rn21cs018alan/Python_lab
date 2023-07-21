c=""

def combine(arr,low,mid,high):
    global c
    i=k=low
    j=mid+1
    while(i<=mid and j<=high):
        if arr[i]<arr[j]:
            c[k]=arr[i]
            i+=1
        else:
            c[k]=arr[j]
            j+=1
        k+=1


    while(i<=mid):
        c[k]=arr[i]
        i+=1
        k+=1
    while(j<=high):
        c[k]=arr[j]
        j+=1
        k+=1
    arr[low:high+1]=c[low:high+1]
        


def Merge(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    Merge(arr,low,mid)
    Merge(arr,mid+1,high)
    combine(arr,low,mid,high)

def MergeSort(arr:list):
    global c
    c=[0]*len(arr)
    Merge(arr,0,len(arr)-1)


def insertion(val:list):
    n=len(val)
    for i in range (1,n):
        v=val[i]
        j=i-1
        while(j>=0 and a[j]>=v):
            val[j+1]=val[j]
            j-=1
        val[j+1]=v

a=[165,22,3,41,4,33,2,1,77,54,3,3,2]
a=[123,14,12,52,5465,23,65,234]
# insertion(a)
MergeSort(a)
print(a)
