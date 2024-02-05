from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch

from elasticsearch import Elasticsearch



app = Flask(__name__)

client = Elasticsearch(
  "https://669154963de240128fcc679400b5110f.centralus.azure.elastic-cloud.com:443",
  api_key="a0I2NEVZMEJpZVhOVkZfc1VLcWU6ZVBVQk1CNWFSSGUtdkdLeE96ODVYUQ=="
)

ELASTICSEARCH_CLOUD_ID = "Weather:Y2VudHJhbHVzLmF6dXJlLmVsYXN0aWMtY2xvdWQuY29tJDY2OTE1NDk2M2RlMjQwMTI4ZmNjNjc5NDAwYjUxMTBmJGIyNTdmOWVjYjMxMTQ2ZDhiNmZiOGViM2Q5NThkYjgx"
ELASTICSEARCH_USERNAME = "elastic"
ELASTICSEARCH_PASSWORD = "7OAzCgxEBgYn4QllK6GydEQO"


ELASTICSEARCH_CLOUD_URL = f"https://669154963de240128fcc679400b5110f.centralus.azure.elastic-cloud.com:443"


client.info()

result = client.search(index="search-weather", q="Bucuresti")

# Define a Flask route to return the search results
@app.route('/')
def index():
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)





