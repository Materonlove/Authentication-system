"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planet, Vehicle, FavoritePeople, FavoritePlanets, FavoriteVehicles
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    users = User.query.all()  #<User Antonio>
    users = list(map(lambda item: item.serialize(), users)) #{name:Antonio, password:123, ....} {name:Usuario2, password:123.... }
    print(users)
  
    return jsonify(users), 200

@app.route('/register', methods=['POST'])
def register_user():
    #recibir el body en json, des-jsonificarlo y almacenarlo en la variable body
    body = request.get_json() #request.json() pero hay que importar request y json

    #ordernar cada uno de los campos recibidos
    email = body["email"]
    name = body["name"]
    password = body["password"]
    is_active = body["is_active"]

    #validaciones
    if body is None:
        raise APIException("You need to specify the request body as json object", status_code=400)
    if "email" not in body:
        raise APIException("You need to specify the email", status_code=400)

    #creada la clase User en la variable new_user
    new_user = User(email=email, name=name, password=password, is_active=is_active)

    #comitear la sesión
    db.session.add(new_user) #agregamos el nuevo usuario a la base de datos
    db.session.commit() #guardamos los cambios en la base de datos

    return jsonify({"mensaje":"Usuario creado correctamente"}), 201 

@app.route('/get-user/<int:id>', methods=['GET'])
def get_specific_user(id):
    user = User.query.get(id)    
  
    return jsonify(user.serialize()), 200

@app.route('/get-user', methods=['POST'])
def get_specific_user2():
    body = request.get_json()   
    id = body["id"]

    user = User.query.get(id)   
  
    return jsonify(user.serialize()), 200

@app.route('/get-user', methods=['DELETE'])
def delete_specific_user():
    body = request.get_json()   
    id = body["id"]

    user = User.query.get(id) 

    db.session.delete(user)
    db.session.commit()  
  
    return jsonify("Usuario borrado"), 200

@app.route('/get-user', methods=['PUT'])
def edit_user():
    body = request.get_json()   
    id = body["id"]
    name = body["name"]

    user = User.query.get(id)   
    user.name = name #modifique el nombre del usuario

    db.session.commit()
  
    return jsonify(user.serialize()), 200



@app.route('/add-favorite/people', methods=['POST'])
def add_favorite_people():
    body = request.get_json() 
    user_id = body["user_id"]
    people_id = body["people_id"]

    character = People.query.get(people.id).first()
    if not character:
        raise APIException('Personaje no encontrado')

    user = People.query.get(user.id).first()
    if not user:
        raise APIException('Usuarios no encontrado')
       

    fav_exist = FavoritePeople.query.filter_by(user_id=user.id, people_id = character.id,)

    if fav_exist:
        raise APIException('el Usuario ya lo tiene guardado en favorito ')


    favorite_people = FavoritePeople(user_id.id, people_id=character.id)
    db.session.add(favorite_people)   
    db.session.commit() 


    return jsonify(favorite_people.serialize()), 200

@app.route('/add-favorite/planets', methods=['POST'])
def add_favorite_planet():
    body = request.get_json() 
    user_id = body["user_id"]
    planet_id = body["planet_id"]


    planet = planet.query.get(planet.id).first()
    if not character:
        raise APIException('Planeta no encontrado') 



    fav_exist = FavoritePlanets.query.filter_by(user_id=user.id, planet_id = planet.id,)

    if fav_exist:
        raise APIException('el Usuario ya lo tiene guardado en favorito ')


    favorite_planets = FavoritePlanets(user_id.id, planet_id=planet.id)
    db.session.add(favorite_planets)   
    db.session.commit() 

    return jsonify(favorite_planets.serialize()), 200


@app.route('/add-favorite/vehicles', methods=['POST'])
def add_favorite_vehicles():
    body = request.get_json() 
    user_id = body["user_id"]
    vehicle_id = nody["vehicle_id"]

    vehicles = Vehicles.query.get(vehicle_id).first()
    if not vehicles:
        raise APIException('vehicle no encontrado')


    fav_exist = FavoriteVehicles.query.filter_by(user_id=user.id, vehicle_id = vehicles.id,) 
    if fav_exist:
        raise APIException('el Usuario ya lo tiene guardado en favorito ')

    favorite_Vehicles = FavoriteVehicles(user_id.id, vehicle_id=vehicles.id)
    db.session.add(favorite_vehicles)   
    db.session.commit() 

    return jsonify(favorite_vehicles.serialize()), 200


@app.route('/favorites', methods=['POST'])
def list_favorites():
    body = request.get_json() 
    user_id = body["user_id"]


    user_favorites = FavoritePeople.query.filter.filter_by(user_id=user.id).all()
    user_favorites_final = map((lambda item: item.serialize(), user_favorites)).all()

    user_favorites_final = user_favorites + user_favorites_final

    user_favorites_planets = FavoritePlanets.query.filter.filter_by(user_id=user.id).all()
    user_favorites_final_planets = map((lambda item: item.serialize(), user_favorites_planets)).all()

    user_favorites_final_planets = user_favorites_planets + user_favorites_final_planets

    user_favorites_vehicles = FavoriteVehicle.query.filter.filter_by(user_id=user.id).all()
    user_favorites_final_vehicles = map((lambda item: item.serialize(), user_favorites_vehicles)).all()

    user_favorites_final_vehicles = user_favorites_vehicles + user_favorites_final_vehicles
    


    return jsonify (user_favorites_finals)


    


    


    


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
