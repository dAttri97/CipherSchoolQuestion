def part1(n):
    for i in range(n,0,-1):
        for j in range(2*i-2):
            print(end=' ')
        for j in range(i,n+1):
            print('*',end=' ')
        print()

def part2(n):
    count,base = 0,ord('A')
    for i in range(n):
        for j in range(i+1):
            print(chr(base+count),end=' ')
            count+=1
        print()

part1(5)
print()
part2(5)