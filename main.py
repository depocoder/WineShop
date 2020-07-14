from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime as dt
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
from pprint import pprint
from collections import defaultdict


excel_data_df = pandas.read_excel('wines.xlsx')
now = dt.now()
wines_categories = excel_data_df.to_dict(orient='record')
sorted_wines =  defaultdict(list)

for wine in wines_categories:
    sorted_wines[wine['Категория']].append(wine)

        

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    year_counter = now.year - 1920,
    wines_categories = sorted_wines,
    types_of_wines = sorted(sorted_wines)
    

)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()