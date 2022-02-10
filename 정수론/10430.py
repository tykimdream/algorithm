# 22.02.10 10430

# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

a, b, c = map(int, input().split())

line1 = (a+b) % c
line2 = ((a % c)+(b % c))
line3 = (a*b) % c
line4 = ((a % c)*(b % c)) % c

print(line1)
print(line2)
print(line3)
print(line4)
