a = [5,9,1,558,3,7,4,-1,-5,-269,5,12]

def sss(arr,inplace=True):

    seg=[False]*len(arr)*4

    def createSeg(pos,l,r,seg,arr):

        if l==r:
            seg[pos]=(arr[l],l)
            return

        mid=(l+r)//2
        createSeg(2*pos+1,l,mid,seg,arr)
        createSeg(2*pos+2,mid+1,r,seg,arr)
        sl=seg[2*pos+1]
        sr=seg[2*pos+2]
        if(sl[0]<sr[0]):
            mn=sl
        else:
            mn=sr
        seg[pos]=mn
        return

    def updateSeg(pos,l,r,seg,val,index):
        if(index<l or index>r):
            return
        if(index==l and index==r):
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
            return False
        if(queryL<=l and queryR>=r):
            return seg[pos]
        mid = (l+r)//2
        a=showSeg(2*pos+1,l,mid,seg,queryL,queryR)
        b=showSeg(2*pos+2,mid+1,r,seg,queryL,queryR)

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

    for i in range(len(arr)-1):
        a=showSeg(0,0,len(arr)-1,seg,i,i)
        b=showSeg(0,0,len(arr)-1,seg,i+1,len(arr)-1)
        if(a[0]>b[0]):
            updateSeg(0,0,len(arr)-1,seg,a[0],b[1])
            updateSeg(0,0,len(arr)-1,seg,b[0],a[1])
    tmp=[]
    for i in range(len(arr)):
        tmp.append(showSeg(0,0,len(arr)-1,seg,i,i)[0])
    if(inplace):
        for i in range(len(arr)):
            arr[i]=tmp[i]
    return tmp


print("array:",a)
newList=sss(a)
print("sorted:",newList)
