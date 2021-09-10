from flask_restful import Resource,reqparse
from re import search
from bcrypt import gensalt, hashpw, checkpw
from models.Usuario import UsuarioModel
from config.conexion_bd import base_de_datos

PATRON_CORREO = r'\w+[@]\w+[.]\w{2,3}'
PATRON_PASSWORD = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#&?])[A-Za-z\d@$!%*#&?]{6,}'

class RegistroController(Resource):
    serializador = reqparse.RequestParser(bundle_errors=True)
    serializador.add_argument(
      'nombre',
      type=str,
      location='json',
      required=True,
      help='Falta el nombre'
    )

    serializador.add_argument(
      'apellido',
      type=str,
      location='json',
      required=True,
      help='Falta el apellido'
    )

    serializador.add_argument(
      'correo',
      type=str,
      location='json',
      required=True,
      help='Falta el correo'
    )

    serializador.add_argument(
      'password',
      type=str,
      location='json',
      required=True,
      help='Falta el password'    
    )

    serializador.add_argument(
      'telefono',
      type=str,
      location='json',
      required=True,
      help='Falta el telefono'    
    )

    def post(self):
      data = self.serializador.parse_args()
      print(data)
      correo = data['correo']
      password = data['password']
      if search(PATRON_CORREO, correo) is None:
        return {
          "message":"Correo incorrecto"
        }, 400
      if search(PATRON_PASSWORD, password)is None:
        return{
          "message":"Password incorrecto, minimo 6 caracteres, una mayuscula, una minuscula, un simbolo especial"
        }, 400
      try:
        nuevoUsuario = UsuarioModel()
        nuevoUsuario.usuarioCorreo = correo
        nuevoUsuario.usuarioNombre = data.get('nombre')
        nuevoUsuario.usuarioApellido = data.get('apellido')
        nuevoUsuario.usuarioTelefono = data.get('telefono')
        # Encriptacion de la contraseña
        # Primero convertimos la pwd a formato bytes
        passwordBytes = bytes(password, "utf-8")
        # llamamos al metodo gensalt que nos dara un salt aleatorio en base al numero de rounds
        salt = gensalt(rounds=10)
        # hashpw que lo que hara sera combinar nuestras pwd con el salt generado previamente
        hashPwd = hashpw(passwordBytes, salt)
        # convertimos el hash a formato string para poder almacenarlo en la bd
        hashPwd = hashPwd.decode('utf-8')
        # almacenamos el hashpwd
        nuevoUsuario.usuarioPassword = hashPwd
        base_de_datos.session.add(nuevoUsuario)
        base_de_datos.session.commit()
        return{
        "message" : "Usuario creado correctamente"
        }, 201
      except Exception as e:  
        base_de_datos.session.rollback()
        return{
          "message" : "Error al ingresar usuario",
          "content": e.args
        }, 500

class LoginController(Resource):
    serializador = reqparse.RequestParser(bundle_errors=True)
    serializador.add_argument(
      'correo',
      type=str,
      location='json',
      required=True,
      help='Falta el telefono'    
    )

    serializador.add_argument(
      'password',
      type=str,
      location='json',
      required=True,
      help='Falta el pasword'    
    )

    def post(self):
      # si el usuario existe en la bd indicarlo,sino en un mensaje indicar indicar que no existe y un estado 404
      data = self.serializador.parse_args()
      usuario = base_de_datos.session.query(UsuarioModel).filter(
        UsuarioModel.usuarioCorreo == data.get('correo')).first()
      if usuario is None:
        return {
          "message":"Usuario no encontrado"
        }, 404
      password = bytes(data.get('password'), 'utf-8')
      usuarioPwd = bytes(usuario.usuarioPassword, 'utf-8')
      print(checkpw(password, usuarioPwd))      
      return {
        "message":"Usuario encontrado"
      }
