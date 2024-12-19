# Documentación del Test

## 1. Descripción general del test

Este test implementa una API REST utilizando **Django** y **Django Rest Framework (DRF)** para gestionar productos (autos). Los endpoints principales permiten acceder a los productos, filtrarlos por categoría y obtener un único producto.

---

## 2. Instrucciones para levantar el proyecto localmente

1. **Clonar el repositorio**:

   ```bash
   git clone <url_del_repositorio>
   ```

2. **Crear un entorno virtual**:
   Asegúrate de tener **Python** y **virtualenv** instalados:

   ```bash
   virtualenv venv
   ```

3. **Instalar las dependencias**:
   Asegúrate de tener **pip** instalado, luego instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el servidor**:
   Ejecuta el servidor con:

   ```bash
   python manage.py runserver
   ```

5. El proyecto estará disponible en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 3. Pruebas locales

Puedes probar la API utilizando las siguientes URLs:

- **Ordenar por precio (descendente)**:

  ```http
  http://127.0.0.1:8000/api/cars/?order_by=price&order_type=desc
  ```

- **Ordenar por precio (ascendente)**:

  ```http
  http://127.0.0.1:8000/api/cars/?order_by=price&order_type=asc
  ```

- **Filtrar por categoría (ejemplo: categoría 2)**:

  ```http
  http://127.0.0.1:8000/api/cars/category/2/
  ```

- **Filtrar por categoría y ordenar por año (descendente)**:

  ```http
  http://127.0.0.1:8000/api/cars/category/1/?order_by=year&order_type=desc
  ```

- **Obtener un único producto por ID (ejemplo: ID 3)**:
  ```http
  http://127.0.0.1:8000/api/cars/3/
  ```

---

## 4. Funcionamiento de la API

### Endpoints:

- **`/api/cars/`**: Devuelve todos los productos.
- **`/api/cars/category/{id}/`**: Filtra los productos por categoría (ID).
- **`/api/cars/{id}/`**: Devuelve un único producto por ID.

### Parámetros:

- **`order_by`**: Define el campo por el cual ordenar los productos. Los valores permitidos son:

  - `price` – Ordena por precio.
  - `year` – Ordena por año.

- **`order_type`**: Define el tipo de orden. Los valores permitidos son:
  - `asc` – Ascendente.
  - `desc` – Descendente.

---

## 5. Administración de Django

### 1. Agregar o editar autos

Puedes usar el panel de administración de Django para agregar, editar o eliminar autos. Aquí te mostramos cómo hacerlo:

1. **Ingresar al panel de administración**:

   - Ve a `http://127.0.0.1:8000/admin`
   - Ingresa con un usuario: 'useradmin' y contraseña: 'admin123123'.

2. **Agregar un auto**:

   - Haz clic en `Cars` en el menú de la izquierda.
   - Selecciona `ADD CAR`.
   - Completa los campos `name`, `price`, `year`, `category`, y otros atributos específicos.
   - Guarda los cambios.

3. **Editar un auto**:
   - Selecciona el auto que deseas editar.
   - Realiza los cambios necesarios en los campos.
   - Guarda los cambios.

### 2. Agregar o editar categorías

Puedes manejar las categorías desde el panel de administración de Django:

1. **Agregar una categoría**:

   - Selecciona `Categories` en el menú de la izquierda.
   - Haz clic en `ADD CATEGORY`.
   - Completa el campo `name`.
   - Guarda los cambios.

2. **Editar una categoría**:
   - Selecciona la categoría que deseas editar.
   - Realiza los cambios necesarios.
   - Guarda los cambios.

---

### Acerca de los datos

Para fines prácticos, este test ha sido desarrollado con solo 4 autos en el sistema.

---

## 6. Consideraciones adicionales

- **Validación de parámetros**:
  - **`order_by`**: Si se pasa un valor distinto a **`year`** o **`price`**, la API devolverá un **400 Bad Request**.
  - **`order_type`**: Si se pasa un valor distinto a **`asc`** o **`desc`**, la API devolverá un **400 Bad Request**.
- En caso de datos incorrectos, como un **ID de categoría** o **producto** no válido, la API devolverá un **404 Not Found**.

---
