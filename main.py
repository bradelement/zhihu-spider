import sys
import json
import urllib
import tornado.httpclient as httpclient
import tornado.ioloop

http_client = httpclient.HTTPClient()

def handle_response(response):
    if response.error:
        return

    body = response.body
    print body
    j = json.loads(body)

    nex = j['paging']['next']
    if nex:
        fetch_url(nex)


def fetch_url(url):
    host = 'https://www.zhihu.com'
    fetch(host+url)


def fetch(url):
    response = http_client.fetch(url)
    handle_response(response)


def generate_url(word):
    host = 'https://www.zhihu.com/r/search'
    params = {
        'q': word,
        'type': 'content',
        'offset': 10,
    }
    return host + '?' + urllib.urlencode(params)


def main():
    for line in sys.stdin:
        url = generate_url(line.strip())
        fetch(url)

    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
