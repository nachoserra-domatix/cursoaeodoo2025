# Añadir seguridad (7)
Hacer dos grupos de usuario, manager y user.
El usuario solo podrá ver y modificar los estudiantes que tenga asignados (crearemos un campo user_id)
El manager podrá crear, borrar ver y modificar cualquier estudiante

# Vistas (9)
Añadir campos notes(html), sequence y responsable(many2one)

## Vista tipo lista:
Añadir campo sequence con widget handle
Mostrar nombre, mail, teléfono, fecha de alta,responsable, cumpleaños y edad
Campo fecha que sea opcional y mostrarlo por defecto (optional show)
Campo responsable que sea opcional pero ocultarlo (optional hide)

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
