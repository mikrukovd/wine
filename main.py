import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from scripts import get_year, get_sorted_drinks

YEAR_OF_FOUNDATION = 1920


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('template.html')

    render_page = template.render(
        year=get_year(datetime.datetime.now().year - YEAR_OF_FOUNDATION),
        sorted_drinks=get_sorted_drinks('wine3.xlsx')
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(render_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
