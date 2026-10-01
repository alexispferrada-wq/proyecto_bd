# 🗺️ Guía Visual: Diagramas de Flujo y Arquitectura
**Proyecto_BD (Django + MySQL / SQLite + Docker)**  
*Documento de apoyo visual especialmente diseñado para estudio neurodivergente (esquemas visuales, mapas de navegación y diagramas de flujo).*

---

## 1. Ciclo de Vida de una Petición (Arquitectura MVT)

```mermaid
sequenceDiagram
    autonumber
    actor U as 🌐 Usuario (Navegador)
    participant URL as 🧭 urls.py
    participant V as ⚙️ views.py
    participant SEC as 🛡️ @login_required
    participant M as 📦 models.py (ORM)
    participant DB as 🗄️ Base de Datos (MySQL / SQLite)
    participant T as 📄 Template (HTML + Bootstrap)

    U->>URL: Clic o enlace (ej: /listado)
    URL->>V: Deriva a mostrarListado()
    V->>SEC: ¿Usuario autenticado?
    alt NO autenticado
        SEC-->>U: Redirige a /login?next=/listado
    else SÍ autenticado
        V->>M: Producto.objects.all().order_by('id')
        M->>DB: SELECT * FROM productos_producto ORDER BY id ASC;
        DB-->>M: Retorna filas de la BD
        M-->>V: Retorna QuerySet de objetos Producto
        V->>T: Inyecta {'productos': productos} en listado.html
        T-->>U: Responde con HTML centrado y formateado
    end
```

---

## 2. Diagrama Entidad - Relación (DER)

```mermaid
erDiagram
    AUTH_USER ||--o{ PRODUCTOS_PRODUCTO : "administra y registra"

    AUTH_USER {
        bigint id PK "Clave primaria autoincrementable"
        varchar username UK "Nombre de usuario único (150 chars)"
        varchar password "Contraseña con hash criptográfico PBKDF2"
        varchar email "Correo electrónico"
        boolean is_superuser "Es administrador del sistema"
        datetime last_login "Fecha y hora del último acceso"
    }

    PRODUCTOS_PRODUCTO {
        bigint id PK "Clave primaria autoincrementable"
        text nombre "Nombre del producto (max 100)"
        text marca "Marca seleccionada (A cuenta, Jumbo, Lider)"
        int precio "Precio en CLP (entero no nulo)"
    }
```

---

## 3. Diagrama de Clases UML

```mermaid
classDiagram
    class User {
        +int id
        +string username
        +string password
        +boolean is_authenticated
        +create_user(username, password) User
    }

    class Producto {
        +int id
        +string nombre
        +string marca
        +int precio
        +__str__() string
    }

    class ProductoAdmin {
        +list_display : ('id', 'nombre', 'marca', 'precio')
        +search_fields : ('nombre', 'marca')
        +list_filter : ('marca',)
    }

    class VistasProductos {
        +registrarUsuario(request) HttpResponse
        +mostrarIndex(request) HttpResponse
        +mostrarListado(request) HttpResponse
        +mostrarFormRegistrar(request) HttpResponse
        +registrarProducto(request) HttpResponse
        +mostrarFormActualizar(request, id) HttpResponse
        +actualizarProducto(request, id) HttpResponse
        +eliminarProducto(request, id) HttpResponse
    }

    User ..> VistasProductos : "inicia sesión / se registra"
    VistasProductos --> Producto : "crea, lee, edita, elimina (ORM)"
    ProductoAdmin --> Producto : "gestiona en /admin/"
```

---

## 4. Mapa Mental de Navegación (Sitemap del Usuario)

```mermaid
graph TD
    A["🔐 /login o /registro<br><b>Pantalla Principal Centrada</b>"] -->|Autenticación Exitosa| B["🏠 / (Menú Principal)<br><b>Bienvenido, usuario!</b>"]
    
    B -->|Clic en Registrar Producto| C["➕ /form_registrar<br><b>Formulario Producto</b>"]
    C -->|POST /registrar| D["📋 /listado<br><b>Tabla CRUD de Productos</b>"]

    B -->|Clic en Ver Listado| D
    
    D -->|Clic en ✏️ Editar| E["✏️ /form_actualizar/:id<br><b>Formulario de Edición</b>"]
    E -->|POST /actualizar/:id| D
    
    D -->|Clic en 🗑️ Eliminar + Confirmación JS| F["🗑️ /eliminar/:id<br><b>Borra registro en BD</b>"]
    F --> D

    D -->|Clic en Menú| B
    C -->|Clic en Menú| B
    E -->|Clic en Volver| D

    B -->|Clic en Cerrar Sesión| G["🚪 POST /logout"]
    G --> A

    classDef login fill:#e7f5ff,stroke:#0d6efd,stroke-width:2px;
    classDef menu fill:#fff9db,stroke:#fab005,stroke-width:2px;
    classDef form fill:#ffffff,stroke:#0d6efd,stroke-width:2px;
    classDef list fill:#ebfbee,stroke:#198754,stroke-width:2px;
    classDef edit fill:#fff3bf,stroke:#fd7e14,stroke-width:2px;
    
    class A login;
    class B menu;
    class C form;
    class D list;
    class E edit;
```

---

## 5. Infraestructura: Docker vs Modo Local

```mermaid
flowchart LR
    subgraph DOCKER["🐳 Modalidad Docker Compose"]
        W["web :8000<br>(Django 5.2)"] <-->|Red interna: db:3306| DB_MYSQL["db :3307<br>(MySQL 8.0)"]
        PMA["phpmyadmin :8080<br>(Gestor Web)"] <-->|Red interna: db:3306| DB_MYSQL
        VOL[("mysql_data<br>Volumen persistente")] --- DB_MYSQL
    end

    subgraph LOCAL["💻 Modalidad Local (Sin Docker)"]
        PY["python manage.py runserver<br>(:8000)"] <--> SQLITE[("db.sqlite3<br>Archivo local")]
    end
```

---

### 📌 Archivo PDF para descargar e imprimir
Encuentra la versión PDF de alta calidad con gráficos vectoriales en:  
👉 **`DIAGRAMAS_Y_FLUJO_VISUAL.pdf`**
