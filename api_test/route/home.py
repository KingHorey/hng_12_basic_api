from datetime import datetime
from flask_restful import Resource


class GetHomePage(Resource):
  def get(self):
    return {
      'email': 'oreoluwaakinbo.oa@gmail.com',
      'current_datetime': datetime.now().isoformat(timespec='seconds') + 'Z',
      'github_url': 'https://github.com/KingHorey/hng_12_basic_api'
    }
