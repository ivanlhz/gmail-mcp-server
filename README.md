# gmail-mcp-server

Servidor para exponer la API de Gmail mediante el Model Context Protocol (MCP), diseñado para su integración con LLMs y uso en entornos como Claude Desktop.

## Requisitos
- Python 3.11 o superior
- [uv](https://github.com/astral-sh/uv) (para la gestión de dependencias y entornos)
- [build](https://pypi.org/project/build/) (solo si quieres empaquetar el módulo)
- [Claude Desktop](https://claude.ai/) (si se va a usar allí)

## Instalación y empaquetado

## Integración con Claude Desktop

Ahora que el proyecto es un módulo instalable, puedes lanzar el servidor usando el comando instalado `gmail-mcp-server`.

Edita tu archivo de configuración de Claude Desktop (por ejemplo, `claude.config.json`) y añade una entrada como la siguiente:

```json
{
  "mcpServers": {
    "gmail": {
      "command": "gmail-mcp-server",
      "env": {
        "GOOGLE_CLIENT_ID": "TU_ID",
        "GOOGLE_CLIENT_SECRET": "TU_SECRET"
      }
    }
  }
}
```

- Cambia `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET` por tus credenciales de Google.
- No necesitas especificar rutas ni argumentos adicionales: el comando `gmail-mcp-server` ejecuta el servidor MCP de Gmail directamente desde cualquier ubicación.

Luego, reinicia Claude Desktop para que detecte y ejecute el servidor MCP.


### 1. Clona el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd gmail-mcp-server
```

### 2. Instala las dependencias del proyecto con uv
```bash
uv pip install -r uv.lock
```

### 3. (Opcional) Instala la herramienta build para empaquetar
```bash
uv pip install build
```

### 4. Empaqueta el módulo
```bash
uv run -m build
```
Esto generará archivos `.whl` y `.tar.gz` en el directorio `dist/`.

### 5. Instala el paquete localmente
```bash
uv pip install dist/gmail_mcp_server-0.1.0-py3-none-any.whl
```
(Asegúrate de ajustar el nombre del archivo `.whl` si cambia la versión.)

### 5. Uso en Claude Desktop
Puedes importar el módulo en tus scripts de Claude Desktop o ejecutarlo como parte de tu flujo de trabajo para exponer la API de Gmail vía MCP.

## Estructura del proyecto
```
.
├── gmail/               # Código fuente del módulo
│   └── __init__.py
├── main.py              # Script principal (puede usarse como entry point)
├── pyproject.toml       # Configuración del paquete
├── README.md            # Este archivo
└── ...
```

## Referencias
- [Guía oficial de empaquetado Python](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Documentación pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

## Gestión de dependencias con uv

Este proyecto utiliza [uv](https://github.com/astral-sh/uv) para gestionar las dependencias y los entornos virtuales, lo que facilita la instalación, el aislamiento y la velocidad de ejecución.

- Para instalar todas las dependencias del proyecto:
  ```bash
  uv pip install -r uv.lock
  ```
- Para instalar nuevas dependencias:
  ```bash
  uv pip install <paquete>
  uv pip freeze > uv.lock
  ```

Consulta la [documentación oficial de uv](https://github.com/astral-sh/uv) para más detalles.

## Notas
- Si deseas publicar el paquete en PyPI, consulta la guía oficial enlazada arriba.
- Puedes crear un entry point para ejecutar el servidor desde la terminal si lo necesitas. Pide ayuda si quieres añadir esta funcionalidad.
