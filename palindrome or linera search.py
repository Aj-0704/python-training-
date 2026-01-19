#palindrome program using two pointer
l1=[1,2,3,4,5,6,1]
start = 0
end = len(l1)-1
while start <= end:
    if (l1[start] != l1[end]):
        print("not palindrome list")
        break
    start += 1
    end -= 1
else:
   print("palindrome list")
#linera search
num = [1,2,3,4,5,4,3,2,1]
i=0
t=7
for _ in num:
    