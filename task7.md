
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

## Modificaciones modelo lineas de cita
* Añadir campo subtotal
  
## Modificaciones modelo de cita
* Añadir campo de total

## Vistas de examenes y resultados
* Vista árbol y formulario para las dos, Kanban y pivot para la que querais
* La vista kanban a vuestro gusto pero intentad añadir la foto de la mascota cuando esté enlazada a una y agrupado por las etapas de adopción

## Filtros en examenes
* Filtro para poder buscar por nombre, profesor, instrumento y curso.
* Haced que el primer filtro de nombre también busque además por curso
* Filtro para saber que examenes han finalizado
* Filtro para saber que examenes todavía no han finalizado.
* Permitir agrupar por profesor.

## Vistas de citas y lineas:
* Añadir subtotal y total en los modelos

## Dominio
En los resultados, al desplegar el many2one de estudiante NO pueden aparecer estudiantes que no están inscritos al curso

# Campos calculados
* Calcular en el modelo de resultados si el estudiante ha aprobado o no
* Botón en exámenes que al pusarlo genere los resultados de aquellos estudiantes que están en ese curso
