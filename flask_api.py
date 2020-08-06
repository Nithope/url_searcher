import url_parser, os
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from flask_pymongo import PyMongo

dbname = os.getenv('DBNAME')
db_uri= os.getenv('DB_URI')

app = Flask(__name__)

app.config['MONGO_DBNAME'] = dbname
app.config['MONGO_URI'] = db_uri

mongo = PyMongo(app)


CORS(app)
api = Api(app)
port=int(os.getenv("PORT",9099))

parser = reqparse.RequestParser()
parser.add_argument("url")


class url(Resource):
  def post(self):
    args = parser.parse_args()
    new_url = args["url"]
    r1=url_parser.search_urls(new_url)
    mongo.db.urls.insert_one(r1)
    return f"URL ADDED TO DB - {url_parser.search_urls(new_url)}"

class list_db(Resource):
  def post(self):
    l_db=url_parser.list_col(mongo.db.urls)
    return f"{l_db}"

class inception_url(Resource):
  def post(self):
    try:
      l_db=url_parser.inception_search(mongo.db.urls.find()[0])
      mongo.db.urls.insert_many(l_db)
      return f"{l_db} - All this info were added in the db"
    except Exception as e:
      return f"An error occurred - {e} "

class drop_col(Resource):
  def post(self):
    mongo.db.urls.drop()
    return f"Collection Dropped"

api.add_resource(url, "/url")
api.add_resource(list_db, "/list_db")
api.add_resource(inception_url, "/inception_url")
api.add_resource(drop_col, "/drop_col")

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=port)