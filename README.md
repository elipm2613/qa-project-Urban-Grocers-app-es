# Sprint 7
## _Qa-project-Urban-Grocers-app-es_

## Creación de un kit para el usuario o usuaria

Vamos a crear un kit dentro de un usuario o usuaria particular. 
Para ello, se siguen estos pasos:

- Envíar una solicitud para crear un nuevo usuario o usuaria com el token de autenticación (authToken).

- Envíar una solicitud para crear un kit personal para este usuario o usuaria.


## Lista de comprobación de pruebas

| Num | Descripcion | Resultado Esperado |
| ------ | ------ | ------ |
| 1 | El número permitido de caracteres (1): kit_body = { "name": "a"} | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 2 | El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} | Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud |
| 3 | 	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": " " } | Código de respuesta: 400 |
| 4 | 	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } | Código de respuesta: 400 |
| 5 | 	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 6 | Se permiten espacios: kit_body = { "name": " A Aaa " } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 7 | Se permiten números: kit_body = { "name": "123" } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 8 | El parámetro no se pasa en la solicitud: kit_body = { } | Código de respuesta: 400 |
| 9 | Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 } | Código de respuesta: 400 |

