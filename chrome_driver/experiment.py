# import uuid
# strings = []
# while len(strings)<=3:
#     post = []
#     for i in range(4):
#         post.append(i)
#     post_string = uuid.uuid1().hex
#     for item in post:
#         post_string +=str(item)+';'
#     strings.append(post_string)
#     print(post_string)
import time


def fun():
    return (1,2)

a= []
c,b=fun()
a.append(c)
a.append(b)
print(a)
time.sleep(0.2)