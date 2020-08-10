import time

def bubble(L):
    for i in range(len(L)-1):
        print("This is the",i,"pass")
        time.sleep(2)
        for j in range(len(L)-1-i):
            time.sleep(2)
            print("j is",L[j],"j+1 is",L[j+1])
            if L[j]>L[j+1]:
                print("swap hoga")
        
                #swap
                L[j],L[j+1]=L[j+1],L[j]
                print("after swap",L)

        print("after the pass",L)
    print(L)


L=[2,8,52,1,24,36]
bubble(L)
