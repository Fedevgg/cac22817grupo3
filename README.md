Nueva configuración para cumplir con la totalidad del projecto:

>> El proyecto debe encontrarse subido a un repositorio git en la nube con acceso a todos los participantes y el docente (pude estar público).

>> Deben existir al menos 3 rutas distintas. (index, contacts, products)
>> - Debe existir al menos una vista parametrizada (products)
- Deben utilizarse templates que cumplan con lo siguiente:
    >> Debe haber al menos un template asociado a una vista.(la mayoría)
    >> Debe existir al menos una relación de herencia entre templates. (de base.html a las demás)
    >> Debe existir al menos un filtro aplicado. (slugify en product_list.html)
    >> Debe existir al menos un template que utilice archivos estáticos (js, css, etc). (Base.html)

- Se deben utilizar Django Forms que cumplan con la siguientes características:
    >> Al menos un formulario debe poseer validaciones en el front-end y en el back-end (contact)
    >> Debe haber al menos un formulario asociado a un template. (contact)
    >> Debe haber al menos un formulario basado en clases. (contact)
    >> Debe haber al menos un formulario asociado a un modelo (contact)

>>Deben existir al menos dos modelos distintos que posean una relación de uno a muchos(Cart_item, etc)
>>El proyecto debe funcionar utilizando un servidor de base de datos local dentro de los soportados (en el curso se recomienda PostgreSQL), y debe poseer las migraciones necesarias para su funcionamiento. (SQLite)
>> Se debe poder acceder al admin de django y al menos un modelo debe poder administrarse desde el admin.(Products)
>>- El proyecto debe poseer al menos una página a la que solo se pueda acceder mediante un usuario autenticado y al misma debe validar tanto en el front-end como en el back-end.

--------------------------------------------------------------------------------------
Objetivos de la página:
    
    Para no logueados:
    - Resumen, catalogo y formulario de contacto
    
    Para logueados:
    - Acceso a precios, ofertas y carrito

    Para staff:
    - Provisorio solo desde el admin de django

Paquetes utilizados:
- Django 3.2
- Pillow
- Jinja2
