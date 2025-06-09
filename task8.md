# Constraint
* Añadir un constraint en curso para que la capacidad no pueda ser negativa.
* Añadir restricción con _sql_constraints en el que el nombre del curso sea único.

# Onchange
* Cambiar la funcionalidad del email del estudiante, quitar el related y añadir un onchange para que cuando se cambie el contacto se traiga el teléfono

# Actions
* Hacer un smartbutton para que en curso aparezcan los exámenes asociadas a ese curso.

# Default
* El estudiante cuando se cree, que tenga un usuario asignado.
* Cuando se cree un curso que se ponga la fecha de hoy como fecha de inicio

# Cron
* Cron que busque los exámenes de manera diaria, si la fecha ha pasado, el estado se pondrá a finalizado


# Deberes
* Un @api.constrains que impida que puedas tener una fecha de de fin de curso anterior a la fecha de inicio
* _sql_constrains en el nombre de habitación, que sea único
* Un onchange al cambiar el profesor del curso, que el campo level se ponga según el que tenga el prfesor.
* Hacer un smartbutton para que en curso aparezcan las lecciones asociadas
* Cuando se cree una lección que por defecto que se ponga la fecha de ese dia
* Cron que busque los cursos y los ponga en finished si la fecha de fin ya ha pasado
