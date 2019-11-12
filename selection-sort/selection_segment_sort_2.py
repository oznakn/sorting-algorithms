a = [5,9,1,558,3,7,4,-1,-5,-269,5,12]


def sss(arr,inplace=True,dbg=False):
    """inplace sorting algo using segment tree construction of
    minimum queries and selection sort algorithm.
    Complexity: O(nlogn)
    The idea is to pick the smallest element in the range [i+1,n-1] and
    swap with the element on the i'th index (if necessary.) """

    seg=[False]*len(arr)*4

    #if(dbg):print(seg)

    def createSeg(pos,l,r,seg,arr):
        """create segment tree recursively"""

        if l==r:
            """base case"""
            seg[pos]=(arr[l],l)
            return

        """recurse to both children"""
        mid=(l+r)//2
        createSeg(2*pos+1,l,mid,seg,arr)
        createSeg(2*pos+2,mid+1,r,seg,arr)
        sl=seg[2*pos+1]
        sr=seg[2*pos+2]
        if(sl[0]<sr[0]):
            mn=sl
        else:
            mn=sr
        """after calculating children, calculate itself"""
        seg[pos]=mn
        return

    def updateSeg(pos,l,r,seg,val,index):
        if(index<l or index>r):
            """out of bounds"""
            return
        if(index==l and index==r):
            """index found, also base case since l==r"""
            seg[pos]=(val,seg[pos][1])
            return
        mid = (l+r)//2
        updateSeg(2*pos+1,l,mid,seg,val,index)
        updateSeg(2*pos+2,mid+1,r,seg,val,index)
        sl=seg[2*pos+1]
        sr=seg[2*pos+2]
        if(sl[0]<sr[0]):
            mn=sl
        else:
            mn=sr
        seg[pos]=mn
        return

    def showSeg(pos,l,r,seg,queryL,queryR):
        if(queryR<l or queryL>r):
            """out of bounds"""
            return False
        if(queryL<=l and queryR>=r):
            """query range fully collides with the interval [l,r]"""
            return seg[pos]
        mid = (l+r)//2
        a=showSeg(2*pos+1,l,mid,seg,queryL,queryR)
        b=showSeg(2*pos+2,mid+1,r,seg,queryL,queryR)

        """if out of bounds, don't make unneccesary comparisons """
        if(not a):
            return b
        if(not b):
            return a

        if(a[0]<b[0]):
            mn=a
        else:
            mn=b
        return mn

    createSeg(0,0,len(arr)-1,seg,arr)

    #if(dbg):print(seg)
    if(dbg):
        for i in range(len(arr)):
            print(showSeg(0,0,len(arr)-1,seg,i,i))

    for i in range(len(arr)-1):
        a=showSeg(0,0,len(arr)-1,seg,i,i)
        b=showSeg(0,0,len(arr)-1,seg,i+1,len(arr)-1)
        if(dbg):print("\nnow in index:",i)
        if(dbg):print(a)
        if(dbg):print("(",b[0],", ",i+1,"-",len(arr)-1,")",sep="")
        if(a[0]>b[0]):
            if(dbg):print(" !! swapping indices",i,"and",b[1])
            updateSeg(0,0,len(arr)-1,seg,a[0],b[1])
            updateSeg(0,0,len(arr)-1,seg,b[0],a[1])
        else:
            if(dbg):print("    ok they are in correct order")
    tmp=[]
    for i in range(len(arr)):
        tmp.append(showSeg(0,0,len(arr)-1,seg,i,i)[0])
    if(inplace):
        for i in range(len(arr)):
            arr[i]=tmp[i]
    return tmp


print("array:",a)
print()
newList=sss(a,dbg=True)
# newList=sss(a)
print("sorted:",newList)
print()
