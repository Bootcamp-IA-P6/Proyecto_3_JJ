20260130064244*

## 📌 Requisitos previos – Instalación de Python
Este proyecto ha sido desarrollado y probado con **Python 3.13.9**.  
Para evitar incompatibilidades, se recomienda usar **esta versión**.
### 🔹 Sistema operativo
- Windows 10 / Windows 11 (64 bits)
---
## 🐍 Instalación de Python 3.13.9 (Windows)
### Opción recomendada: Instalación desde python.org
1. Abre tu navegador y ve a: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
```url
https://www.python.org/downloads/windows/
```
2. Busca **Python 3.13.9** (64-bit).
3. Descarga el instalador:	[`Windows installer (64-bit)`](https://www.python.org/ftp/python/3.13.9/python-3.13.9-amd64.exe)
```url
https://www.python.org/ftp/python/3.13.9/python-3.13.9-amd64.exe
```
---
### 🔧 Instalación paso a paso
1. Ejecuta el instalador descargado.
2. **MUY IMPORTANTE**: marca estas opciones antes de continuar:
    - ✅ **Add Python to PATH**
    - ✅ **Install launcher for all users** (opcional pero recomendable)
3. Pulsa **Install Now**.
4. Espera a que finalice la instalación.
---
### ✅ Verificación de la instalación
Nota: python puede apuntar a varias versiones como por ejemplo:
Regex para eliminar líneas vacías en Notepad++: `^\s*$\n`
#### Ejecutables relacionados con Python en Windows
##### `py.exe`
- **Python Launcher para Windows** (modo consola).
- Selecciona automáticamente la versión de Python según argumentos, `shebang` o configuración.
- Recomendado para scripts multiplataforma (`#!/usr/bin/env python`).
---
##### `pymanager.exe`
- **Gestor interno del Python Launcher**.
- Utilizado para administración de instalaciones Python (normalmente no se invoca manualmente).
- Apoya la detección y selección de versiones.
---
##### `python.exe`
- **Intérprete estándar de Python (CLI)**.
- Abre consola interactiva o ejecuta scripts `.py`.
- Bloquea la terminal hasta finalizar el proceso.
---
#####`python3-64.exe`
- Intérprete Python **versión 3**, **64 bits**.
- Alias explícito para evitar ambigüedad con Python 2 (histórico).
- No siempre presente en todas las instalaciones.
---
##### `python3.13.exe`
- Intérprete Python **versión 3.13.x**.
- Útil para pruebas o proyectos fijados a una versión concreta.
- Consola activa (stdout/stderr visibles).
---
##### `python3.14-64.exe`
- Intérprete Python **versión 3.14.x**, **64 bits**.
- Instalación específica por arquitectura.
- Ideal para entornos que requieren consistencia binaria.
---
##### `python3.14.exe`
- Intérprete Python **versión 3.14.x** (arquitectura según instalación).
- Similar a `python.exe` pero versionado explícitamente.
---
##### `python3.exe`
- Alias genérico de **Python 3**.
- Puede apuntar a la versión 3 “predeterminada” del sistema.
- Útil en scripts y automatización.
---
##### `pythonw.exe`
- Intérprete Python **sin consola** (Windows GUI mode).
- Usado para aplicaciones gráficas (Tkinter, PyQt, etc.).
- No muestra salida por terminal.
---
##### `pythonw3-64.exe`
- Python GUI (`pythonw`) **versión 3**, **64 bits**.
- Pensado para aplicaciones gráficas modernas.
---
##### `pythonw3.13.exe`
- Python GUI **versión 3.13.x**.
- Sin ventana de consola.
---
##### `pythonw3.14-64.exe`
- Python GUI **versión 3.14.x**, **64 bits**.
- Ideal para apps gráficas en entornos productivos.
---
##### `pythonw3.14.exe`
- Python GUI **versión 3.14.x** (arquitectura según instalación).
- Variante sin consola del intérprete versionado.
---
##### `pythonw3.exe`
- Alias genérico de **Python 3 GUI**.
- Selecciona la versión gráfica predeterminada.
---
##### `pyw.exe`
- **Python Launcher en modo GUI**.
- Equivalente a `py.exe`, pero sin consola.
- Respeta `shebang` y configuración del launcher.
---
##### `pywmanager.exe`
- **Gestor del launcher GUI**.
- Parte del subsistema de selección de intérprete sin consola.
- Uso principalmente interno.
---
Abre una terminal (CMD, PowerShell o Git Bash) y ejecuta:
`python --version`
La salida debe ser:
`Python 3.13.9`
Si ves otra versión:
- revisa que no haya otra instalación anterior de Python
- o que el `PATH` esté correctamente configurado
---
## 🧪 Comprobación adicional (opcional)
Para confirmar la ruta del intérprete:
### En Git Bash
`which python`
### En CMD / PowerShell
`where python`
Debe apuntar a una ruta asociada a Python 3.13.
---
## ℹ️ Nota importante sobre versiones
- Versiones anteriores de Python **pueden no ser compatibles** con algunas dependencias del proyecto.
- Se recomienda **no usar Python 3.12 o inferior** para evitar problemas con:
    - Django
    - Selenium
    - dependencias tipadas
## 1. Configuración inicial y entorno virtual
El proceso comienza con la **creación de la estructura base del proyecto** y la **preparación de un entorno virtual aislado**, con el objetivo de mantener las dependencias del proyecto separadas del Python global del sistema y evitar conflictos entre versiones o librerías.
Se trabaja explícitamente con **Python 3.13.9**, garantizando coherencia con el resto del desarrollo y las herramientas utilizadas.
### Pasos realizados
- Se crea el directorio raíz del proyecto y se accede a él:
```bash
mkdir webscraper
cd webscraper
# Se inicializa el archivo .gitignore para definir, desde el inicio, qué archivos o carpetas no deben versionarse (por ejemplo, el entorno virtual):
touch .gitignore
# Se crea un entorno virtual utilizando la versión específica de Python 3.13.9:
python3.13 -m venv .venv
# Se activa el entorno virtual en un entorno Windows con Git Bash, asegurando que los comandos posteriores utilicen el intérprete aislado:
source .venv/Scripts/activate
# Se verifica la versión activa de Python para confirmar que el entorno virtual está correctamente configurado:
python --version
# Este paso establece una base reproducible y controlada sobre la que se construirá el resto del proyecto.
```
```bash
cat > .gitignore
# Entorno virtual
.venv/

# Python
__pycache__/
*.pyc

# Variables de entorno
.env

# IDEs
.vscode/
.idea/

# Archivos temporales de Microsoft Office
~$*.docx
```
---
## 2. Instalación de Django y creación del proyecto
En esta fase se instala el **framework Django** dentro del **entorno virtual activo** y se genera la **estructura base del proyecto web**.  
El objetivo es disponer de un esqueleto funcional sobre el que empezar a desarrollar la aplicación.
### Directorio de trabajo correcto
Para ejecutar `pip install django` debes encontrarte en:
```path
~/Proyectos/webscraper
```
Es decir, la raíz del proyecto, con el entorno virtual .venv activado.
El directorio concreto no afecta técnicamente a pip, pero hacerlo desde la raíz facilita la gestión de dependencias (requirements.txt).
Pasos realizados
Instalación de Django en el entorno virtual:
```bash
pip install django
```
Creación del proyecto Django:
```bash
django-admin startproject webscraper_project
```
Acceso al directorio del proyecto:
```bash
cd webscraper_project
```
Estructura del proyecto generada (desde webscraper)
```tree
webscraper/
├── README.md                         # Documentación inicial del proyecto
├── requirements.txt                  # Dependencias del proyecto (Django, etc.)
├── .venv/                            # Entorno virtual (no versionado)
└── webscraper_project/
    ├── manage.py                     # Utilidad principal de administración Django
    ├── db.sqlite3                    # Base de datos SQLite por defecto
    ├── scraper/                      # Aplicación Django principal
    │   ├── __init__.py               # Marca el directorio como paquete Python
    │   ├── admin.py                  # Registro de modelos en el admin de Django
    │   ├── apps.py                   # Configuración de la app `scraper`
    │   ├── models.py                 # Definición de modelos de datos
    │   ├── views.py                  # Vistas (lógica de respuesta HTTP)
    │   ├── tests.py                  # Tests de la aplicación
    │   ├── migrations/               # Control de cambios en la base de datos
    │   │   ├── __init__.py            # Inicialización del paquete migrations
    │   │   └── 0001_initial.py        # Migración inicial de modelos
    │   ├── services/                 # Lógica de negocio desacoplada
    │   │   ├── __init__.py            # Inicialización del paquete services
    │   │   ├── scrape.py              # Lógica principal de scraping
    │   │   ├── scrape_inline.py       # Variante de scraping inline
    │   │   └── scrape_ChatGPT_Corregido.py # Versión corregida/iterada del scraping
    │   └── management/               # Comandos personalizados de Django
    │       ├── __init__.py            # Inicialización del paquete management
    │       └── commands/
    │           ├── __init__.py        # Inicialización del paquete commands
    │           └── scraper.py         # Comando personalizado (`python manage.py scraper`)
    └── webscraper_project/            # Configuración global del proyecto
        ├── __init__.py                # Marca el paquete del proyecto
        ├── settings.py                # Configuración principal de Django
        ├── urls.py                    # Definición de rutas (URL routing)
        ├── asgi.py                    # Punto de entrada ASGI (async)
        └── wsgi.py                    # Punto de entrada WSGI (deploy clásico)
```
Observación técnica
La estructura refleja una separación clara entre configuración del proyecto y lógica de aplicación, siguiendo buenas prácticas Django:
webscraper_project/ (interno): configuración global.
 · scraper/: dominio funcional del scraping.
 · services/ y management/commands/: desacoplo de lógica y automatización.

Repasar:

find . \
  -type d \( \
    -name ".git" -o \
    -name ".venv" -o \
    -name "__pycache__" \
  \) -prune -o \
  -type f \( \
    -name "*.py" -o \
    -name "*.md" -o \
    -name "manage.py" -o \
    -name "requirements.txt" -o \
    -name "db.sqlite3" \
  \) -print
./README.md
./requirements.txt
./webscraper_project/db.sqlite3
./webscraper_project/manage.py
./webscraper_project/scraper/admin.py
./webscraper_project/scraper/apps.py
./webscraper_project/scraper/management/commands/scraper.py
./webscraper_project/scraper/management/commands/__init__.py
./webscraper_project/scraper/management/__init__.py
./webscraper_project/scraper/migrations/0001_initial.py
./webscraper_project/scraper/migrations/__init__.py
./webscraper_project/scraper/models.py
./webscraper_project/scraper/services/scrape.py
./webscraper_project/scraper/services/scrape_ChatGPT_Corregido.py
./webscraper_project/scraper/services/scrape_inline.py
./webscraper_project/scraper/services/__init__.py
./webscraper_project/scraper/tests.py
./webscraper_project/scraper/views.py
./webscraper_project/scraper/__init__.py
./webscraper_project/webscraper_project/asgi.py
./webscraper_project/webscraper_project/settings.py
./webscraper_project/webscraper_project/urls.py
./webscraper_project/webscraper_project/wsgi.py
./webscraper_project/webscraper_project/__init__.py


**Si quieres, el siguiente paso natural sería documentar:
**registro de la app en INSTALLED_APPS
**primer comando manage.py runserver
**flujo completo de un comando de scraping
**Dime cómo continuamos.

## 3. Gestión de dependencias y control de versiones
En esta fase se consolidan **las dependencias del proyecto** y se establece el **control de versiones con Git**, garantizando trazabilidad, reproducibilidad y una base sólida para el trabajo colaborativo.  
Todo el proceso se realiza **con el entorno virtual activado** y desde la **raíz del proyecto `webscraper`**.
---
### Instalación de dependencias de scraping
Se instalan las librerías necesarias para la automatización de navegadores y la gestión de drivers:
```bash
pip install selenium
pip install webdriver-manager
```
A continuación, se congela el estado exacto de las dependencias instaladas:
```bash
pip freeze > requirements.txt
```
Esto permite recrear el entorno en cualquier otro sistema mediante pip install -r requirements.txt.
### Inicialización del repositorio Git
Se inicializa el repositorio local y se prepara el proyecto para su versionado:
```bash
git init
```
Configuración de .gitignore
El archivo .gitignore se ajusta para excluir elementos que no deben versionarse, como:
Entorno virtual:
.venv/
Archivos temporales de Microsoft Office:
~$*.docx
### Primer commit del proyecto
Se añade el estado actual del proyecto al área de staging y se realiza el commit inicial:
```bash
git add .
git commit -m "Estado inicial del proyecto webscraper"
```
Este commit representa una línea base estable del proyecto.
### Subida del trabajo a la rama develop
Siguiendo una estrategia de ramas tipo Git Flow, cada commit local se sincroniza con la rama develop del repositorio remoto en GitHub.
Pasos estándar tras cada commit
Crear (si no existe) y cambiar a la rama develop:
```bash
git checkout -b develop
```
**(Si ya existe, usar git checkout develop)
### Vincular el repositorio local con el remoto (solo la primera vez):
```bash
git remote add origin https://github.com/Jose-JulioRamirezySanchez-Escobar/<nombre-del-repositorio>.git
```
### Subir los cambios a la rama develop:
```bash
git push -u origin develop
```
### A partir de este momento, tras cada nuevo commit bastará con:
```bash
git push
```
Resultado del proceso
Al finalizar esta fase se dispone de:
Dependencias controladas y versionadas (requirements.txt)
Repositorio Git inicializado y limpio
Historial de cambios coherente
Rama develop sincronizada con el repositorio remoto
Este punto marca el inicio formal del desarrollo controlado del proyecto webscraper.
**Si quieres, el siguiente paso lógico sería documentar:
**la estrategia de ramas completa (develop / feature / main)
**o el flujo de trabajo diario con commits y PRs

## Creación y vinculación de un repositorio remoto desde Git Bash

Sí, **es posible crear el repositorio remoto directamente desde Git Bash**, pero **no con Git “puro”**.  
Para ello se utiliza la **CLI oficial de GitHub**, que permite **autenticarse, crear repositorios y operar remotamente** sin salir de la terminal.

La herramienta recomendada es **:contentReference[oaicite:0]{index=0} CLI (`gh`)**.

---

## Enfoque correcto (resumen)

- ❌ `git remote add origin ...` **NO crea** repositorios remotos  
- ✅ `gh repo create` **SÍ crea** el repositorio en GitHub
- ✅ Todo el flujo puede hacerse desde **Git Bash**, tras autenticación

---

## Pasos completos desde Git Bash

### 1. Instalar GitHub CLI (`gh`)
*(solo una vez en el sistema)*

```bash
winget install --id GitHub.cli
```
Verificación:
```bash
gh --version
```
2. Autenticarse contra GitHub
```bash
gh auth login
```
Selección recomendada:
Account: GitHub.com
Protocol: HTTPS
Authentication: Browser
Authorize GitHub CLI ✔️
📌 Tras esto, Git Bash queda autorizado para operar remotamente.

3. Situarse en la raíz del proyecto local
cd ~/Proyectos/webscraper
Asegúrate de que:
El repositorio Git está inicializado (git init)
Hay al menos un commit
4. Crear el repositorio remoto desde Git Bash
```bash
gh repo create webscraper \
  --public \
  --source=. \
  --remote=origin \
  --push
```
Qué hace exactamente:
Crea webscraper en tu cuenta de GitHub
Lo vincula como origin
Sube automáticamente la rama actual
5. (Opcional) Usar rama develop como flujo principal
```bash
git checkout -b develop
git push -u origin develop
```
A partir de aquí:
```bash
git push
```
es suficiente tras cada commit.

#### Alternativa: crear repo remoto SIN subir código
```bash
gh repo create webscraper --public
git remote add origin https://github.com/Jose-JulioRamirezySanchez-Escobar/webscraper.git
git push -u origin develop
```
Útil si quieres más control manual.
Flujo típico a partir de ahora
# trabajar
```bash
git add .
git commit -m "Mensaje claro"
```
# sincronizar
```bash
git push
```
Conclusión técnica
✔️ Sí, puedes crear repositorios remotos desde Git Bash
✔️ La autenticación se gestiona una sola vez
✔️ gh convierte Git Bash en un cliente remoto completo
✔️ Ideal para flujos profesionales (Git Flow, PRs, automatización)
Si quieres, el siguiente paso natural sería documentar:
el flujo feature → develop → main
o la automatización de releases y tags
Dime cómo continuamos.

https://github.com/Jose-JulioRamirezySanchez-Escobar/webscraper.git