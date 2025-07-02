# Opciones m2o

En Curso no se debe de poder acceder al profesor ni crear profesores nuevos de manera rápida.
En Instrumento no se debe de poder crear una familia nueva, solo elegir.

# Modelo nuevo asistencia a realizar en una lección

Vamos a crear por una parte un modelo nuevo llamado asistencia. Este modelo va a ser un one2many para las lecciones.

Va a tener un campo de secuencia, estudiante, un check de asistencia y un campo fecha y hora

# Vista embembida

Vamos a añadir este modelo como vista embebida en lección

# Contexto

Vamos a decir desde contexto, que el campo por defecto de fecha de la asistencia sea el mismo el de la lección
