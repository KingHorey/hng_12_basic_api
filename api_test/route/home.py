from datetime import datetime
from flask_restful import Resource


class GetHomePage(Resource):
  def get(self):
    return {
      'email': 'oreoluwaakinbo.oa@gmail.com',
      'current_datetime': datetime.now().isoformat(),
      'url': 'https://hng-12-basic-api.onrender.com'
    }
