import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from scripts import get_year, get_drinks_info

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('template.html')


render_page = template.render(
    year=get_year(datetime.datetime.now().year - 1920),
    drinks=get_drinks_info()
)


with open('index.html', 'w', encoding='utf8') as file:
    file.write(render_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
