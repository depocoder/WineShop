from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime as dt
from jinja2 import Environment, FileSystemLoader, select_autoescape

now = dt.now()

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    year_count = now.year - 1920
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()