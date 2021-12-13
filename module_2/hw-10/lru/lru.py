import requests
import redis


def get_data_from_api(city):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q": city}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "657c063b24msh72cef233e9d263cp108acajsn3ebd15378fc9"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


def get_data_from_cache(data, client):
    result = client.get(data)
    return result


def redis_cache_check(data, city, client):
    info = get_data_from_cache(data, client)

    if info:
        info_decode = info.decode('utf-8')
        return f'Data from cache\n' \
               f'{info_decode}'

    client.set(city, info)

    return f'Data from API\n' \
           f'{info}'


# def main(city, client):
#     data_from_api = get_data_from_api(city)
#     data_from_cache = get_data_from_cache(data_from_api, client)
#     print(get_data_from_cache(data_from_api, client))
    # print(data_from_cache.keys)
    # if data_from_cache:
    #     info_decode = data_from_cache.decode('utf-8')
    #     return print(f'Data from cache\n'
    #                  f'{info_decode}')
    #
    # client.set(city, data_from_api)
    #
    # return print(f'Data from API\n'
    #              f'{data_from_api}')


if __name__ == '__main__':
    redis_client = redis.StrictRedis(host='localhost', port='6381', db=0)

    print(get_data_from_cache('London', redis_client))
    print(redis_client.keys())
