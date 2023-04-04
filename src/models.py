from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    favorite_people =db.relationship('FavoritePeople', backref = 'user', lazy=True)
    favorite_vehicles =db.relationship('FavoriteVehicles', backref = 'user', lazy=True)
    FavoritePlanets =db.relationship('FavoritePlanets', backref = 'user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    mass = db.Column(db.String(80), unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    birth_year = db.Column(db.String(80), unique=False, nullable=False)
    FavoritePeople =db.relationship('FavoritePeople', backref = 'people', lazy=True)

    def serialize(self):
        return {
            "id": self.id,        
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    diameter = db.Column(db.String(250), unique=False, nullable=False)
    gravity = db.Column(db.String(250), unique=False, nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.String(250), nullable=False)
    FavoritePlanets =db.relationship('FavoritePlanets', backref = 'planet', lazy=True)


    def serialize(self):
        return {
            "id": self.id,        
            "name": self.name,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water
            

            
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    model = db.Column(db.String(250), unique=False, nullable=False)
    length = db.Column(db.String(250), unique=False, nullable=False)
    crew = db.Column(db.String(250), unique=False, nullable=False)
    starship_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    max_atmosphering_speed = db.Column(db.String(250), nullable=False)
    hyperdrive_rating = db.Column(db.String(250), nullable=False)
    MGLT = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250), nullable=False)
    consumables = db.Column(db.String(250), nullable=False)
    pilots = db.Column(db.String(250), nullable=False)
    FavoriteVehicles =db.relationship('FavoriteVehicles', backref = 'vehicle', lazy=True)
    
   
            
            

    def serialize(self):
        return {
            "id": self.id,        
            "name": self.name,
            "model": self.model,
            "length": self.length,
            "crew": self.crew,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "passengers": self. passengers,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "pilots": self.pilots,
            "pilots": self.pilots

            
        
            # do not serialize the password, its a security breach
        }

class FavoritePeople(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False) 
    




    def serialize(self):
        return {
            "id": self.id,    
            "user_id": self.user_id,    
            "people_id": self.people_id,
            "people_name": People.query.get(self.people_id).serialize()["name"],
            "user_name": user.query.get(self.user_id).serialize()["name"],
            "user":User.query.get(self.user_id),
            "people":People.query.get(self.people_id).serialize()

            


           
            
          
            # do not serialize the password, its a security breach
        } 


        

class FavoritePlanets (db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False) 
    




    def serialize(self):
        return {
            "id": self.id,    
            "user_id": self.user_id,    
            "planet_id": self.planet_id,
            "planets_name": People.query.get(self.people_id).serialize()["name"],
            "user_name": user.query.get(self.user_id).serialize()["name"],
            "user":User.query.get(self.user_id),
            "planets":People.query.get(self.people_id).serialize()
            
            
          
            # do not serialize the password, its a security breach
        } 


class FavoriteVehicles (db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False) 
   




    def serialize(self):
        return {
            "id": self.id,    
            "user_id": self.user_id,    
            "vehicle_id": self.vehicle_id,
            "vehicles_name": People.query.get(self.people_id).serialize()["name"],
            "user_name": user.query.get(self.user_id).serialize()["name"],
            "user":User.query.get(self.user_id),
            "vehicles":People.query.get(self.people_id).serialize()
            
          
            # do not serialize the password, its a security breach
        } 