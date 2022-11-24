Nueva configuración para cumplir con la totalidad del projecto:

(cumplido) - El proyecto debe encontrarse subido a un repositorio git en la nube con acceso a todos los participantes y el docente (pude estar público).

(cumplido) - Deben existir al menos 3 rutas distintas. (index, contacts, products)
(a terminar) - Debe existir al menos una vista parametrizada (products)
- Deben utilizarse templates que cumplan con lo siguiente:
    > (cumplido) Debe haber al menos un template asociado a una vista.
    > (cumplido) Debe existir al menos una relación de herencia entre templates. (de base.html a las demás)
    > (cumplido) Debe existir al menos un filtro aplicado. (slugify en product_list.html)
    > (cumplido) Debe existir al menos un template que utilice archivos estáticos (js, css, etc). (Base.html)

- Se deben utilizar Django Forms que cumplan con la siguientes características:
    > Al menos un formulario debe poseer validaciones en el front-end y en el back-end
    > Debe haber al menos un formulario asociado a un template. (contact)
    > (cumplido) Debe haber al menos un formulario basado en clases. 
    > (cumplido) Debe haber al menos un formulario asociado a un modelo 

- Deben existir al menos dos modelos distintos que posean una relación de uno a muchos  
- (provisorio SQLite) El proyecto debe funcionar utilizando un servidor de base de datos local dentro de los soportados (en el curso se recomienda PostgreSQL), y debe poseer las migraciones necesarias para su funcionamiento. 
- (cumplido) Se debe poder acceder al admin de django y al menos un modelo debe poder administrarse desde el admin.(Products)
- El proyecto debe poseer al menos una página a la que solo se pueda acceder mediante un usuario autenticado y al misma debe validar tanto en el front-end como en el back-end.

--------------------------------------------------------------------------------------
To-do
- (Fernando) Acomodar el carousel de index.html a modo que tomo imagenes de la media_root
- (Fernando) Acomodar products_patterns a modo de que levante la DetailView
- (Luciana) Formulario de registro (idCliente, passCliente)
- (Iran) Relación 1 a muchos carrito de compras-> acceso a carrito de compras (pkProducto, cantidad, precio)
- (Fede) Acomodar el css del nav para que muestre el boton desplegable
- (Fede) Hacer que el formulario de contacto se conecte con la DB

--------------------------------------------------------------------------------------
Objetivos de la página:
- Muestrario de productos
- Operaciones de usuario/Mail de contacto

Paquetes utilizados:
- Django 3.2
- Pillow
- Jinja2
