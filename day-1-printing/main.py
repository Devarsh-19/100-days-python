def check(x, y):
    if (x+y) % 4 == 0:
        return True
    return False


def main():
    
    T = int(input())
    flist = list()
    for i in range(0,T):
        n = int(input())
        lst = list(map(int,input().strip.split()))[:n]
        for i in range(0,n+1):
            for j in range(i,n+1):
                ans = check(i,j)
                if(ans):
                    flist.append(list(i,j))
                    
    print(flist)


if __name__ == "__main__":
    main()
