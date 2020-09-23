import requests


def ss():
    url_request = "http://10.208.209.81:5040/api/v1/tts/results/wav/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDA4Mzg0MjcsImlhdCI6MTYwMDgzNDgyNywiaXNzIjoic3MiLCJjdG4iOiI1ODg1ODY2MTcxNTZiNDE3NWZiYzNkOTk1NzhiYjc5YjFjNDAyZGZhN2RmNDNlMGU5ZDkzNGM4ZjlkYTYxYWEyIiwibW9kIjoibWFsZV9ub3J0aCIsImN0eCI6ImdlbmVyYWwifQ.NBdz69nKRfrNwQqmg_MikPJhlqNfDwjjA8lNrjDnp5M"
    response = requests.get(url_request)
    data = response.content
    print data


ss()
