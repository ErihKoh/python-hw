import redis

# r.mset('firstname' 'Jack' 'lastname' 'Stuntman' 'age' '35')
# print(r.keys())

# r.set('1', 5)
# g = r.get('1')
# r.set('1', 'abs')
# g = r.get('1')
# print(g.decode('utf-8'))
queue_list = []


def set_in_redis(elm, client):
    if elm in queue_list:
        queue_list.remove(elm)
        queue_list.insert(0, elm)
    else:
        queue_list.insert(0, elm)

    if len(queue_list) > 5:
        queue_list.pop()

    for idx, i in enumerate(queue_list):
        client.set(idx, i)

    return print(f'{elm} has been added to redisDB')


def get_from_redis(key, client):
    data = client.get(key).decode('utf-8')
    queue_list.remove(data)
    queue_list.insert(0, data)

    for idx, i in enumerate(queue_list):
        client.set(idx, i)

    return f'key {key}: {data}'


def get_all_data_from_redis(client):
    for i in range(5):
        print(client.get(i).decode('utf-8'))


if __name__ == '__main__':
    redis_client = redis.StrictRedis(host='localhost', port='6381', db=0)

    set_in_redis('a', redis_client)
    set_in_redis('b', redis_client)
    set_in_redis('c', redis_client)
    set_in_redis('d', redis_client)
    set_in_redis('e', redis_client)
    set_in_redis('f', redis_client)
    set_in_redis('h', redis_client)
    set_in_redis('hello', redis_client)

    print(get_all_data_from_redis(redis_client))
    print(get_from_redis('3', redis_client))
    print(get_all_data_from_redis(redis_client))
