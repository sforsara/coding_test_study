import sys
sys.stdin=open("input.txt", "r") 

def DFS(L, sum):   
    if L == n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0) 
    if sum>total//2:
       return 
    else:
       DFS(L+1, sum+a[L])
       DFS(L+1, sum)
   



if __name__== "__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total = sum(a)
    DFS(0) 
    print("NO")
   



    










    



    


    


