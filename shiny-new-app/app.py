import aiohttp
import uvicorn
from fastapi import FastAPI


app = FastAPI()


class BeerDataProvider:
    favorite_beer_url = 'https://api.sampleapis.com/beers/ale/1'

    @staticmethod
    def _transform_data(beer_data: dict):
        beer_data['rating']['average'] = round(beer_data['rating']['average'], 2)
        return beer_data

    async def get_favorite_beer(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.favorite_beer_url) as resp:
                beer_data = await resp.json()
        return self._transform_data(beer_data)


@app.get('/api/beers/favorite')
async def get_favorite_beer():
    return await BeerDataProvider().get_favorite_beer()


if __name__ == '__main__':
    uvicorn.run(app)
