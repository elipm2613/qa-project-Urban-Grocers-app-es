import data
import sender_stand_request

# esta función cambia los valores en el parámetro "name"
def get_kit_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body


def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

# Función de prueba positiva
def positive_assert(kit_body):
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    # Comprueba si el código de estado es 201
    assert response.status_code == 201
    # Comprueba que el campo name está en la respuesta y contiene un valor
    assert response.json()["name"] == kit_body["name"]

# Función de prueba negativa
def negative_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response

    # Comprueba si el código de estado es 400
    assert response.status_code == 400



def test1_crear_un_kit_con_1_caracter():
    new_kit_body = get_kit_body("a")
    positive_assert(new_kit_body)

def test2_crear_un_kit_con_numero_permitido_de_caracteres():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(new_kit_body)

def test3_crear_un_kit_con_numero_menor_permitido_de_caracteres():
    new_kit_body = get_kit_body(" ")
    negative_assert(new_kit_body)

def test4_crear_un_kit_con_numero_mayor_permitido_de_caracteres():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(new_kit_body)

def test5_crear_un_kit_con_caracteres_especiales():
    new_kit_body = get_kit_body("№%@,#&")
    positive_assert(new_kit_body)

def test6_crear_un_kit_con_espacios():
    new_kit_body = get_kit_body("A aaa")
    positive_assert(new_kit_body)

def test7_crear_un_kit_con_numeros_de_caracteres():
    new_kit_body = get_kit_body("123")
    positive_assert(new_kit_body)

def test8_crear_un_kit_con_ningun_parametro():
    new_kit_body = get_kit_body()
    negative_assert(new_kit_body)

def test9_crear_un_kit_con_numeros_en_el_nombre():
    new_kit_body = get_kit_body(123)
    negative_assert(new_kit_body)
