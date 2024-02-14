from flask import Flask
import requests


app = Flask(__name__)


class BeerDataProvider:
    favorite_beer_url = 'https://api.sampleapis.com/beers/ale/1'

    @staticmethod
    def _transform_data(beer_data: dict):
        beer_data['rating']['average'] = round(beer_data['rating']['average'], 2)
        return beer_data

    def get_favorite_beer(self):
        beer_data = requests.get(self.favorite_beer_url).json()
        return self._transform_data(beer_data)


@app.route('/api/beers/favorite')
def get_favorite_beer():
    return BeerDataProvider().get_favorite_beer()


if __name__ == '__main__':
    app.run()
