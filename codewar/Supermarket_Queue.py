"""There is a queue for the self-checkout tills at the supermarket.
Your task is write a function to calculate the total time required for all the customers to check out!
input
customers: an array of positive integers representing the queue.
Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
"""

customers, n = ([2,3,10], 2)

# def queue_time(customers, n):
#     timeshop1 = []
#     timeshop = 0
#     if n == 1:
#         timeshop += sum(customers)
#         return timeshop
#     elif n > 1:
#         if n > len(customers):
#             n = len(customers)
#         for i in range(0, n):
#             timeshop1.append(customers[i])
#
#         count = n
#         min = timeshop1[0]
#         k = 0
#         while count < len(customers):
#             for j in range(len(timeshop1)):
#                 if min > timeshop1[j]:
#                     min = timeshop1[j]
#                     k = j
#             min += customers[count]
#             count += 1
#             timeshop1[k] = min
#         return max(timeshop1)




def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

print(queue_time(customers, n))