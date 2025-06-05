
## Modelo nuevo de Exámenes
* Nombre
* Curso
* Fecha y hora
* Instrumento
* Puntuación mínima para aprobar
* Puntuación máxima
* Estado
* Profesor evaluador
* Resultados (one2many)

## Modelo nuevo de resultados del examen
* Examen
* Estudiante
* Nota/Puntuación
* Aprobado (bool) / o un selector de suspendido/aprobado
* Comentarios del profesor

## Vistas de examenes y resultados
* Vista árbol y formulario la de examenes y kanban

## Filtros en examenes
* Filtro para poder buscar por nombre, profesor, instrumento y curso.
* Haced que el primer filtro de nombre también busque además por curso
* Filtro para saber que examenes han finalizado
* Filtro para saber que examenes todavía no han finalizado.
* Permitir agrupar por profesor.

## Dominio
En los resultados, al desplegar el many2one de estudiante NO pueden aparecer estudiantes que no están inscritos al curso

# Campos calculados
* Calcular en el modelo de resultados si el estudiante ha aprobado o no
* Botón en exámenes que al pusarlo genere los resultados de aquellos estudiantes que están en ese curso
