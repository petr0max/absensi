from wsgiref.simple_server import make_server


def application(environ, start_response):
    body = '<h2>Hello WSGI</h2>'
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(body)))
    ]
    start_response(status, headers)
    return