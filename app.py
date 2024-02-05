from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
import json
from flask import Flask, render_template, request, jsonify


es = Elasticsearch(
    cloud_id="Weather:Y2VudHJhbHVzLmF6dXJlLmVsYXN0aWMtY2xvdWQuY29tJDY2OTE1NDk2M2RlMjQwMTI4ZmNjNjc5NDAwYjUxMTBmJGIyNTdmOWVjYjMxMTQ2ZDhiNmFmYjhlYjNkOTU4ZGI4MQ=="
)

app = Flask(__name__, template_folder='templates')


ELASTICSEARCH_CLOUD_ID = "Weather:Y2VudHJhbHVzLmF6dXJlLmVsYXN0aWMtY2xvdWQuY29tOjQ0MyQ2NjkxNTQ5NjNkZTI0MDEyOGZjYzY3OTQwMGI1MTEwZiRiMjU3ZjllY2IzMTE0NmQ4YjZmYjhlYjNkOTU4ZGI4MQ=="
ELASTICSEARCH_USERNAME = "elastic"
ELASTICSEARCH_PASSWORD = "7OAzCgxEBgYn4QllK6GydEQO"

ELASTICSEARCH_CLOUD_URL = f"https://weather.es.centralus.azure.elastic-cloud.com"

es = Elasticsearch(
    cloud_id=ELASTICSEARCH_CLOUD_ID,
    basic_auth=(ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD),
)


# Index weather data from JSON file
@app.route('/upload_weather', methods=['POST'])
def upload_weather():
    with open('weather_data.json', 'r') as file:
        weather_data = json.load(file)

    for data_entry in weather_data:
        es.index(index='search-weather', body=data_entry)

    return jsonify({'message': 'Weather data uploaded successfully'}), 201

# Display data from the 'search-weather' index for a specific city
@app.route('/display_weather', methods=['GET', 'POST'])
def display_weather():
    if request.method == 'POST':
        
        city = request.form.get('city')

        if not city:
            return render_template('result.html', city_data=[], error='City parameter is missing')

        city = city.strip()  

        print(f"Searching for data for city: {city}")

        # Use the city parameter in the Elasticsearch query
        result = es.search(index='search-weather', body={
            "query": {
                "match": {
                    "city": city  
                }
            }
        })

        print(result)  

        hits = result.get('hits', {}).get('hits', [])

        displayed_data = []
        for hit in hits:
            displayed_data.append(hit['_source'])

        return render_template('result.html', city_data=displayed_data)

    # If the request method is GET, render the initial search form
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)