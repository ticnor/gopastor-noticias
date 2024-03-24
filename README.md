# Noticias GO Pastor

Las noticias se encuentran en ficheros `.md` dentro de `posts`. Se recomienda organizarlas en carpetas
en formato `año-mes`.

## Cómo añadir una noticia

1. Navegar a [`posts`](https://github.com/ticnor/gopastor-noticias/tree/master/posts). 
2. Si ya existe carpeta para el año/mes, entrar en ella.
3. Hacer clic en "Add file" y seleccionar "Create new file".
4. Poner nombre al fichero, terminado en `.md` (recomendado `año-mes-día identificador.md`). 
  Si no existía carpeta para el año mes, el nombre deberá llevar `año-mes/` antes
  (p.e., `año-mes/año-mes-día identificador.md`).
5. Copiar el contenido de [`plantilla.md`](https://github.com/ticnor/gopastor-noticias/blob/master/plantilla.md),
   y actualizar los valores.
6. Hacer clic en "Commit changes...". Se pueden dejar los valores por defecto (o introducir un texto personalizado).
7. Si se han incluido imágenes (ver [Contenido de las noticias](#contenido-de-las-noticias)), se pueden subir
   de manera similar con Add file -> Upload files.

## Contenido de las noticias

La plantilla tiene unas líneas de metadatos con 3 campos:

* `title`: El título de la noticia
* `date`: La fecha de la noticia en formato `año-mes-día`
* `image`: Opcionalmente, se puede usar para añadir imágenes a la noticia (1 por línea).

A continuación, **es necesario dejar una línea completamente en blanco**, tras lo que vendrá el cuerpo de la noticia.
Este texto se puede introducir en formato [Markdown](https://daringfireball.net/projects/markdown/). Se pueden
emplear [Dillinger.io](https://dillinger.io/) or [Editor.md](https://pandao.github.io/editor.md/en.html) para
facilitar la tarea.