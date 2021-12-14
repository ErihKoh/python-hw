import httpx
import redis


def get_data_from_api(name):

    with httpx.Client() as web_client:
        base_url = 'https://api.nationalize.io?name'
        url = f'{base_url}={name}'
        response = web_client.get(url)
        code_country = response.json()['country'][0]['country_id']

    return f'name: {name} from country: {code_country}'


def get_data_from_cache(name, client):
    result = client.get(name)
    return result


def main(name, client):
    info = get_data_from_cache(name, client)

    if info:
        info_decode = info.decode('utf-8')
        return print(f'Data from cache\n'
                     f'{info_decode}')
    info_from_api = get_data_from_api(name)

    client.set(name, info_from_api)

    return print(f'Data from API\n'
                 f'{info_from_api}')


if __name__ == '__main__':
    redis_client = redis.StrictRedis(host='localhost', port='6381', db=0)

    main('John', redis_client)
    main('Mark', redis_client)
    main('Joshua', redis_client)
    main('Ivan', redis_client)
    main('Petro', redis_client)


