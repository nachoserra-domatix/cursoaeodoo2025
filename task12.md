# Crear modulo nuevo


# Herencia por extensión
* Añadir a curso un producto y un precio de curso
* En el modulo nuevo heredar el modelo de curso y añadir un one2many de pedidos de venta
* Heredar curso y añadir botón de crear pedido de venta. Crear tantos pedidos como estudiantes.
* Heredar sale.order y añadirle el curso asociada en otra información.

# Heredar método
* Heredar método de crear y añadir una secuencia a los cursos (Ojo con la compañía, si no os funciona es por que tenéis una compañía distinta a la de la secuencia)

# Herencia por delegación
* En el modelo de estudiante que tenemos añadirle herencia por delegación con inherits y probar después a añadir a la vista campos de res.partner como por ejemplo street,city y country_id

# Deberes
* Añadir botón de cancelar (y estado nuevo de cancelado al curso) en el módulo original
* Heredar el botón de cancelar curso(en el módulo nuevo, para que si se cancela se cancelen los pedidos)
* Añadir botón en en curso que confirme la venta y facture el pedido asociado
* Herencia por delegación en profesor (contacto)

