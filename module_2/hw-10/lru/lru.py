import redis

r = redis.StrictRedis(host='localhost', port='6381', db=0)

r.mset('firstname' 'Jack' 'lastname' 'Stuntman' 'age' '35')
print(r.keys())

# r.set('1', 5)
# g = r.get('1')
# r.set('1', 'abs')
# g = r.get('1')
# print(g.decode('utf-8'))
# cache = {}
# queue_list = []


# def lru(elm):
#     if len(queue_list) == 0:
#         queue_list.append(elm)
#
#     if elm in queue_list:
#         queue_list.remove(elm)
#         queue_list.insert(0, elm)
#     if len(queue_list) > 4:
#         queue_list.pop()
#
#     queue_list.insert(0, elm)
#     cache = {idx: i for idx, i in enumerate(queue_list)}
#     return cache
#
#
# print(lru(1))
# lru(3)
# lru(4)
# lru(5)
# lru(6)
# lru(7)
# print(lru(3))
# print(lru(1))
