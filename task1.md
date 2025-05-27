# Añadir seguridad (7)
Hacer dos grupos de usuario, manager y user.
El usuario solo podrá ver y modificar los estudiantes que tenga asignados (crearemos un campo user_id)
El manager podrá crear, borrar ver y modificar cualquier cita

Hacer reglas para que un estudiante solo pueda ser visto por su responsable si el grupo es usuario. (para esto antes es necesario crear el user_id en estudiantes)

# Vistas (9)
Añadir campos notes(html), sequence y responsable(many2one)

## Vista tipo lista:
Añadir campo sequence con widget handle
Mostrar nombre, fecha de alta,responsable, y estado
Campo fecha que sea opcional y mostrarlo por defecto
Campo responsable que sea opcional pero ocultarlo

## Vista formulario
Nombre h1 como en pedidos y dos columnas:
Activo email, teléfono y responsable, cumpleaños y edad


## Solapas:
Notas

# Ejercicio
## Modelo music.school.instrument
* Crear vistas de lista y de formulario, algún campo como optional show
* Añadir al ir.model.access.csv los grupos de user y manager
* Añadir solapa para la descripcion del instrumento
