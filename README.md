# gmail-mcp-server

[![GitHub stars](https://img.shields.io/github/stars/ivanlhz/gmail-mcp-server?style=social)](https://github.com/ivanlhz/gmail-mcp-server/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/ivanlhz/gmail-mcp-server)](https://github.com/ivanlhz/gmail-mcp-server/issues)
[![GitHub forks](https://img.shields.io/github/forks/ivanlhz/gmail-mcp-server?style=social)](https://github.com/ivanlhz/gmail-mcp-server/network/members)
[![MIT License](https://img.shields.io/github/license/ivanlhz/gmail-mcp-server)](https://github.com/ivanlhz/gmail-mcp-server/blob/master/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/release/python-3110/)

Repositorio oficial: [https://github.com/ivanlhz/gmail-mcp-server](https://github.com/ivanlhz/gmail-mcp-server)

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

## Obtener credenciales de Google (GOOGLE_CLIENT_ID y SECRET)

Para que el servidor pueda acceder a la API de Gmail, necesitas crear credenciales OAuth 2.0 en Google Cloud:

1. Ve a la [Google Cloud Console](https://console.cloud.google.com/).
2. Crea un nuevo proyecto o selecciona uno existente.
3. Ve a "APIs y servicios" > "Biblioteca" y busca "Gmail API". Haz clic en "Habilitar".
4. Ve a "APIs y servicios" > "Credenciales" y haz clic en "Crear credenciales" > "ID de cliente de OAuth".
5. Selecciona "Aplicación de escritorio" como tipo de aplicación.
6. Asigna un nombre y haz clic en "Crear".
7. Descarga el archivo JSON, ábrelo y copia los valores de `client_id` y `client_secret`.
8. Usa estos valores como variables de entorno `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET` al lanzar el servidor.

Más información en la [guía oficial de Google](https://developers.google.com/identity/protocols/oauth2?hl=es).

## Integración con Claude Desktop y otros clientes MCP

### Windows
- El ejecutable se encuentra en:
  ```
  C:\Users\<usuario>\develop\proyectos\mcp\gmail-mcp-server\.venv\Scripts\gmail-mcp-server.exe
  ```
- Puedes ejecutarlo directamente desde esa ruta o añadir `.venv\Scripts\` al PATH para poder usar `gmail-mcp-server` desde cualquier terminal.
- **Si has añadido la carpeta de scripts al PATH** (recomendado):
  Ahora puedes usar simplemente `gmail-mcp-server` como comando global en cualquier terminal.
- **Recomendación para Claude Desktop:**
  En tu configuración (por ejemplo, `claude.config.json`):
  - Si NO tienes el PATH configurado:
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
  - Si SÍ tienes el PATH configurado:
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
- Cambia `<usuario>` por tu nombre de usuario de Windows y completa tus credenciales.

### Mac/Linux
- El ejecutable se encuentra en:
  ```
  /ruta/a/tu/proyecto/.venv/bin/gmail-mcp-server
  ```
- Puedes ejecutarlo directamente desde esa ruta.

**Para agregar el ejecutable al PATH de forma permanente:**
1. Abre tu archivo de configuración de shell (`~/.bashrc`, `~/.zshrc`, etc.).
2. Añade la línea:
   ```bash
   export PATH="/ruta/a/tu/proyecto/.venv/bin:$PATH"
   ```
3. Guarda el archivo y ejecuta `source ~/.bashrc` o `source ~/.zshrc` (según tu shell), o reinicia la terminal.

Ahora podrás usar simplemente `gmail-mcp-server` como comando global.

- **Recomendación para Claude Desktop:**
  - Si NO tienes el PATH configurado:
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
  - Si SÍ tienes el PATH configurado:
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
- Cambia `/ruta/a/tu/proyecto/` por la ruta real y completa tus credenciales.

- Tras cualquier cambio, reinicia Claude Desktop para que detecte y ejecute el servidor MCP correctamente.

## Referencias
- [Guía oficial de empaquetado Python](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Documentación pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Google API Python Client (Gmail)](https://googleapis.github.io/google-api-python-client/docs/dyn/gmail_v1.html)
- [google-auth](https://google-auth.readthedocs.io/en/latest/)
- [dotenv (python-dotenv)](https://saurabh-kumar.com/python-dotenv/)
- [mcp[cli] (Model Context Protocol CLI)](https://modelcontextprotocol.io/docs/cli)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/)

## Comunidad y contribución

- ¿Tienes dudas, sugerencias o encontraste un bug? Abre un [issue](https://github.com/ivanlhz/gmail-mcp-server/issues).
- ¿Quieres contribuir? Haz un fork y envía tu pull request. ¡Las contribuciones son bienvenidas!
- Para cualquier consulta, también puedes abrir una discusión en la pestaña [Discussions](https://github.com/ivanlhz/gmail-mcp-server/discussions) del repositorio.

## Notas
- Si deseas publicar el paquete en PyPI, consulta la guía oficial enlazada arriba.
- Puedes crear un entry point para ejecutar el servidor desde la terminal si lo necesitas. Pide ayuda si quieres añadir esta funcionalidad.
