from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime as dt
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
from pprint import pprint

excel_data_df = pandas.read_excel('wines.xlsx')
now = dt.now()
wines = excel_data_df.to_dict(orient='record')
sorted_wines = {
    'Белые вина':{}, 
    'Красные вина':{},
    'Напитки':{}}



for item in wines:
    if item['Категория']=='Белые вина':
        sorted_wines['Белые вина'] =  sorted_wines['Белые вина'] + item 
    elif item['Категория']=='Красные вина':
        sorted_wines['Красные вина'] = sorted_wines['Красные вина'] + item 
    else:
        sorted_wines['Напитки'] = item
print(sorted_wines)

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    year_count = now.year - 1920,
    

)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()