# # problem 02:
# N = 21
#
# if N%2==0:
#     if (N>=2 and N<=5):
#         print("Not Weird")
#     elif (N>=6 and N<=20):
#         print("Weird")
#     else:
#         print("Not Weird")
# else:
#     print("Weird")

# # problem "loop "
#
# for i in range(5):
#     print(i*i)

# # problem "loop + if-elif-else".......lipe year
#
# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if year%100==0:
#         if year%400==0:
#             leap = True
#     elif year%4==0:
#         leap = True
#
#     return leap
#
# year = int(input())
# print(is_leap(year))


# # problem """ valo """
# #
# # if __name__ == '__main__':
# #     n = int(input())
# # for i in range(n):
# #     print(i+1,end="")


# # problem list_comprehantion
#
#
# ## x = int(input())
# # y = int(input())
# # n = int(input())
# x=2
# y=2
# z=2
# n=2
# ar = [ [i,j,k]for i in range(x+1)  for j in range(y+1) for k in range(z+1) if i+j+k!=n ]
# # p = 0
# # for i in range(x + 1):
# #     for j in range(y + 1):
# #         for k in range(z+1):
# #              if i + j +k != n:
# #                  ar.append([])
# #                  ar[p] = [i, j,k]
# #                  p += 1
# print(ar)
#


# # problem """Find the Runner-Up Score!"""
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
# print(sorted(list(set(arr)))[-2])

# #prolem : nested loop
# name=[]
# score=[]
# for _ in range(int(input())):
#     name.append(input())
#     score.append(float(input()))
# newlist = []
# for i in range(len(name)):
#     newlist.append([name[i],score[i]])
# s=sorted(score)
# for i in  range(len(newlist)):
#
#     if float(s[0])==float(newlist[i][1]):
#         print(newlist[i][0])
#         s.remove(s[0])


# #problem : Finding the percentage
# # 2
# # Harsh 25 26.5 28
# # Anurag 26 28 30
# # Harsh
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] =float( sum(scores)/len(scores))
#     query_name = input()
#
# print(format(student_marks.get(query_name), '.2f'))



# import turtle
#
# turtle.shape("turtle")
# c=turtle.Screen()
# a=turtle.Turtle()
# a.speed(3)
# b=True
#
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)


# import turtle
#
# turtle.color("black")
# turtle.speed(3)
#
# counter =0
#
# while counter<36:
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.right(10)
#     counter +=1
#
#
#
# turtle.exitonclick()

# # break and continue .....................................................................
#
# terminate_program= False
#

# while not terminate_program:
#     number1=int( input("Please enter a number : "))
#     number2= int(input("Please enter anather number : "))
#
#     while True :
#         operation =input("Please enter add /sub or quit to exit : ")
#
#         if operation=="quit":
#             terminate_program=True
#             break
#         if operation not in ["add", "sub"]:
#             print("Unknown operation !")
#             continue
#         if operation =="add":
#             print("Result is : ", number1+number2)
#             break
#         if operation=="sub":
#             print("Result is :",number1-number2)
#             break


# # list collection..........................................................................
#
# if __name__ == '__main__':
#     N = int(input())
#
# mylist=[]
# for i in range(N):
#
#     stringList=input().split()
#
#
#     if stringList[0] == 'insert':
#         mylist.insert(int(stringList[1]) ,int(stringList[2]))
#     elif stringList[0]== "print":
#         print(mylist)
#     elif stringList[0] == "remove":
#         mylist.remove(int(stringList[1]))
#     elif stringList[0]== "append":
#         mylist.append(int(stringList[1]))
#     elif stringList[0]== 'sort':
#         mylist.sort()
#     elif stringList[0]=='pop':
#         mylist.pop()
#     elif stringList[0]== 'reverse':
#         mylist.reverse()

# tuples


if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))

    print(hash(integer_list))












