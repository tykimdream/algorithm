T = int(input())
for test_case in range(1, T+1):
   N = int(input())
   arr = list(map(int, input().split()))
   arr.sort()
   print("#{}".format(test_case), end = ' ')
   for i in range(N):
       print(arr[i], end = ' ')
   print()