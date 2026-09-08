from connectToMySQL import connectToMySQL

class registro:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

 
@classmethod
def save(cls, data):
    query = "INSERT INTO registros (nombre, apellido, edad) VALUES (%(nombre)s, %(apellido)s, %(edad)s);"
    return connectToMySQL('registro').query_db(query, data)


classmethod
def get_all(cls):
    query = "SELECT * FROM registros;"
    results = connectToMySQL('registro').query_db(query)
    registros = []
    for registro in results:
        registros.append(cls(registro))
    return registros
