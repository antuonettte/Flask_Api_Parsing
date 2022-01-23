from flask import Flask, jsonify, abort
from flask_restful import Api, Resource, reqparse
import json
from pprint import pprint as pp

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, help="Name of recipe required.", required=True)
parser.add_argument('ingredients', type=list, help="Ingredients of recipe required", required=True)
parser.add_argument('instructions', type=list, help="Instructions of recipe required", required=True)

url = open('./app/data.json')

data = json.load(url)

app = Flask(__name__)
api = Api(app)

recipeNames = []


class FetchRecipes(Resource):

    def get(self):

        names = []

        for recipe in data['recipes']:
            names.append(recipe['name'])

        return {'recipeNames': names}, 200

    def post(self):

        newData = parser.parse_args()

        for recipe in temp['recipes']:
            recipeNames.append(recipe['name'])

        print(recipeNames)

        if newData['name'] not in recipeNames:

            temp['recipes'].append(newData)

        else:
            return {"error": "Recipe already exists"}, 400

        pp(temp)

        return 201

    def put(self):

        newData = parser.parse_args()

        for recipe in data['recipes']:
            recipeNames.append(recipe['name'])

        if newData['name'] in recipeNames:

            data['recipes'].append(newData)

        else:
            return {"error": "Recipe Doesn't Exist"}, 404

        return 201


temp = data


class Recipe(Resource):

    def get(self, name):


        for rec in data['recipes']:
            for k, v in rec.items() :
                
                if type(v) == str and v.lower() == name.lower():
                    print(v + name)

                    return {
                        "details": {
                            "ingredients": [ing for ing in rec['ingredients']],
                            'numSteps': len(rec['instructions'])
                        }
                    }, 200

        return {}, 200


api.add_resource(FetchRecipes, "/recipes")
api.add_resource(Recipe, "/recipes/details/<string:name>")
# api.add_resource(PutRecipe, "/recipes")

if __name__ == "__main__":
    app.run(debug=True)
