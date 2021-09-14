from flask import Flask, current_app
from flask_restful import Api
from config.conexion_bd import base_de_datos
from models.Tarea import TareaModel
from controllers.Tarea import TareaController
from controllers.Usuario import (RegistroController,
                                 UsuarioController,
                                 ResetearPasswordController)
from flask_jwt import JWT
from config.seguridad import autenticador, identificador
from dotenv import load_dotenv
from datetime import timedelta, datetime
from os import environ
from config.configuracion_jwt import manejo_error_JWT

load_dotenv()

app = Flask(__name__)
api = Api(app)

# config => las variables de configuracion de mi proyecto de flask DEBUG=TRUE, PORT= 5000, ENVIRONMENT=DEVELOPMENT
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# contraseña de la token
app.config['SECRET_KEY'] = environ.get('JWT_SECRET')
# cambia la fecha de expiracion de la token expresado en timedelta
app.config['JWT_EXPIRATION_DELTA'] = timedelta(minutes=30)
# cambia el parametro en el cual se pedira el nombre del usuario
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
# cambia el endpoint en el cual se hara la authentication
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_AUTH_HEADER_PREFIX'] = 'BEARER'

jsonwebtoken = JWT(app=app, authentication_handler=autenticador,
                   identity_handler=identificador)


jsonwebtoken.jwt_error_callback = manejo_error_JWT

base_de_datos.init_app(app)
base_de_datos.create_all(app=app)


@jsonwebtoken.jwt_payload_handler
def definir_payload(identity):
    # print(identity)
    # print(app.config)
    #  “iss” (Issuer) Claim: Creador del token.
    # “sub” (Subject) Claim: Sujeto del token.
    # “aud” (Audience) Claim:  Audiencia del token (a quien va dirigido).
    # ”exp” (Expiration Time) Claim: Tiempo de expiración.
    # “nbf” (Not Before) Claim: No antes de (tiempo desde que debe ser aceptado).
    # “iat” (Issued At) Claim: Creado a (tiempo en el que fue creado).
    # “jti” (JWT ID) Claim: JWT Id (identificador único).
    creation = datetime.utcnow()
    expiration = creation + current_app.config.get('JWT_EXPIRATION_DELTA')
    not_before_delta = creation + \
        current_app.config.get('JWT_NOT_BEFORE_DELTA')
    user = {
        "id": identity.id,
        "correo": identity.username
    }
    print(current_app.config.get('JWT_EXPIRATION_DELTA'))    

    return {
        "iat": creation,
        "exp": expiration,
        "nbf": not_before_delta,        
        "usuario": user
    }


# RUTAS
api.add_resource(RegistroController, '/registro')
# api.add_resource(LoginController, '/login')
api.add_resource(UsuarioController, '/usuario')
api.add_resource(TareaController, '/tareas')
api.add_resource(ResetearPasswordController, '/reset-password')

if __name__ == '__main__':
    app.run(debug=True)