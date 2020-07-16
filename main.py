from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime as dt
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
from pprint import pprint
from collections import defaultdict
import argparse

parser = argparse.ArgumentParser(description='dir for your excel file')
parser.add_argument('indir', type=str,default = 'wines.xlsx', nargs="?", help='Specify the path to the folder in which lies excel file')
filepatch = parser.parse_args()
    
if filepatch.indir != "wines.xlsx":
    filepatch.indir = filepatch.indir


excel_data_df = pandas.read_excel(filepatch.indir, na_values=' ', keep_default_na=False)
wines_categories = excel_data_df.to_dict(orient='record')
now = dt.now()
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
    drinks_categories = sorted(sorted_wines.items())
    
)


with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()