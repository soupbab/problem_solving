# p.178 위에서 아래로 ####################################################################################################

n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

for number in reversed(sorted(numbers)):
    print(number, end=" ")

# p.180 성적이 낮은 순서로 학생 출력하기 ####################################################################################

n = int(input())
scores = {}

for i in range(n):
    name, score = input().split()
    scores[name] = int(score)

answer = sorted(scores, key=lambda x: x[1], reverse=True)

for name in answer:
    print(name, end=" ")

# p.182 두 배열의 원소 교체 ###############################################################################################

n, k = map(int, input().split())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

array_A.sort()
array_B.sort(reverse=True)

for i in range(k):
    if array_A[i] < array_B[i]:
        array_A[i], array_B[i] = array_B[i], array_A[i]
    else:
        break

print(sum(array_A))

########################################################################################################################
