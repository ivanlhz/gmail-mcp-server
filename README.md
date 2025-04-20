# gmail-mcp-server

Servidor para exponer la API de Gmail mediante el Model Context Protocol (MCP), diseñado para su integración con LLMs y uso en entornos como Claude Desktop.

## Descripción
Este proyecto permite exponer la API de Gmail vía MCP, facilitando su integración con LLMs y uso en entornos como Claude Desktop.

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

## Requisitos
- Python 3.11 o superior
- [uv](https://github.com/astral-sh/uv) (para la gestión de dependencias y entornos)
- [build](https://pypi.org/project/build/) (solo si quieres empaquetar el módulo)
- [Claude Desktop](https://claude.ai/) (si se va a usar allí)

## Instalación de dependencias
1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd gmail-mcp-server
   ```
2. Instala las dependencias del proyecto con uv:
   ```bash
   uv pip install -r uv.lock
   ```

## Construcción y empaquetado
1. (Opcional) Instala la herramienta build:
   ```bash
   uv pip install build
   ```
2. Empaqueta el módulo:
   ```bash
   uv run -m build
   ```
   Esto generará archivos `.whl` y `.tar.gz` en el directorio `dist/`.

## Instalación local del paquete
Instala el paquete en tu entorno:
```bash
uv pip install dist/gmail_mcp_server-0.1.0-py3-none-any.whl
```
(Asegúrate de ajustar el nombre del archivo `.whl` si cambia la versión.)

## Gestión de dependencias con uv
Este proyecto utiliza [uv](https://github.com/astral-sh/uv) para gestionar las dependencias y los entornos virtuales.

- Instalar todas las dependencias del proyecto:
  ```bash
  uv pip install -r uv.lock
  ```
- Instalar nuevas dependencias:
  ```bash
  uv pip install <paquete>
  uv pip freeze > uv.lock
  ```

Consulta la [documentación oficial de uv](https://github.com/astral-sh/uv) para más detalles.

## Integración con Claude Desktop y otros clientes MCP

### Windows
- El ejecutable se encuentra en:
  ```
  C:\Users\<usuario>\develop\proyectos\mcp\gmail-mcp-server\.venv\Scripts\gmail-mcp-server.exe
  ```
- Puedes ejecutarlo directamente desde esa ruta o añadir `.venv\Scripts\` al PATH para poder usar `gmail-mcp-server` desde cualquier terminal.
- **Recomendación para Claude Desktop:**
  En tu configuración (por ejemplo, `claude.config.json`):
  ```json
  {
    "mcpServers": {
      "gmail": {
        "command": "C:\\Users\\<usuario>\\develop\\proyectos\\mcp\\gmail-mcp-server\\.venv\\Scripts\\gmail-mcp-server.exe",
        "env": {
          "GOOGLE_CLIENT_ID": "TU_ID",
          "GOOGLE_CLIENT_SECRET": "TU_SECRET"
        }
      }
    }
  }
  ```
- Cambia `<usuario>` por tu nombre de usuario de Windows y completa tus credenciales.

### Mac/Linux
- El ejecutable se encuentra en:
  ```
  /ruta/a/tu/proyecto/.venv/bin/gmail-mcp-server
  ```
- Puedes ejecutarlo directamente desde esa ruta o añadir `.venv/bin/` al PATH para usar `gmail-mcp-server` desde cualquier terminal.
- **Recomendación para Claude Desktop:**
  En tu configuración:
  ```json
  {
    "mcpServers": {
      "gmail": {
        "command": "/ruta/a/tu/proyecto/.venv/bin/gmail-mcp-server",
        "env": {
          "GOOGLE_CLIENT_ID": "TU_ID",
          "GOOGLE_CLIENT_SECRET": "TU_SECRET"
        }
      }
    }
  }
  ```
- Cambia `/ruta/a/tu/proyecto/` por la ruta real y completa tus credenciales.

- Si añades la carpeta de scripts (`.venv\Scripts\` en Windows, `.venv/bin/` en Mac/Linux) al PATH, podrás usar simplemente `gmail-mcp-server` como comando.
- Tras cualquier cambio, reinicia Claude Desktop para que detecte y ejecute el servidor MCP correctamente.

## Referencias
- [Guía oficial de empaquetado Python](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Documentación pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Google API Python Client (Gmail)](https://googleapis.github.io/google-api-python-client/docs/dyn/gmail_v1.html)
- [google-auth](https://google-auth.readthedocs.io/en/latest/)
- [dotenv (python-dotenv)](https://saurabh-kumar.com/python-dotenv/)
- [mcp[cli] (Model Context Protocol CLI)](https://modelcontextprotocol.io/docs/cli)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/)

## Notas
- Si deseas publicar el paquete en PyPI, consulta la guía oficial enlazada arriba.
- Puedes crear un entry point para ejecutar el servidor desde la terminal si lo necesitas. Pide ayuda si quieres añadir esta funcionalidad.
