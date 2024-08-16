Proyecto Final Pablo Blanco

- En este proyecto se busca cumplir los puntos de la consigna a partir de dos aplicaciones:
    
    Users: en la misma se administran los usuarios, puediendo registrarse, loguearse, cambiar el avatar, actualizar los datos y cambiar la contraseña. Solo los superuser pueden borrar usuarios.

    Books: esta es la aplicación principal y es donde se guardan los modelos propios. Para hacerlo mas desafiante, elegí hacer un CRUD de dos modelos relacionados (además del CRUD de usuarios) de manera tal de tener una especie de blog de mensajes, tal como solicita la consigna, en una tabla de registros que existen en el modelo principal. La descripcion es la siguiente:
        a) El primer modelo es el de LIBROS (clase Book) que tiene su nombre, autor, una breve reseña del libro y una imagen de portada. Todos estos datos son editables por un usuario administrador ya que es el único que tiene privilegios para modificar los libros.
        b) La otra clase es de VALORACIONES (clase Review) que contiene el usuario que la creo, en que fecha, el comentario acerca del libro y una puntuacion entre 0 y 5 para otorgarle. En este caso, el usuario puede editar y borrar sus propios post, mientras que el administrador puede editar los suyos y borrar (solo borrar, no editar) el de otros usuarios. Esto lo pense para cumplir un rol de "moderador" en caso que algun comentario de libro fuera inapropiado.

- En todo el trabajo intente seguir el consejo de nombres en ingles para las clases y las vistas, url, templates.

- Las dudas que se fueron presentando durante el trabajo, las trate de solucionar con lo visto en clases y mucho Stack Overflow. De hecho hay un tema puntual que explico en el video, que me costo mucho encontrar porque no estaba haciendo el prompt correcto. Asi que como experiencia, fue muy enriquecedora. Por supuesto que todo es mejorable y seguramente existen maneras mas eficientes de hacerlo, pero desde mi punto de vista el trabajo cumple con lo que quise hacer y me quedo muy satisfecho con la entrega.

- El proyecto se ejecuta en un entorno virtual e incluye el archivo de requerimientos.

- Quedo atento a cualquier modificacion que consideren necesaria.
