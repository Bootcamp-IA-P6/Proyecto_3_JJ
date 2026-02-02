## Propósito:
Poder crear archivos MarkDown a partir de una Lista.txt.
Lista.txt debe ser generada con las rutas desde las que se va a ejecutar la macro.
He llamado a la macro bucle5.sh (proviene de la evolución de anteriores macros).
Para crear el archivo Lista.txt podría ejecutarse el comando:

```bash
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
  \) -print \
> Lista1.txt
```

```Bash
Coder@F5-LAPMAD-124 MINGW64 ~/Proyectos/webscraper (develop)
$ find . \
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
  \) -print \
> Lista1.txt

Coder@F5-LAPMAD-124 MINGW64 ~/Proyectos/webscraper (develop)
$ cat !$
cat Lista1.txt
./colorful_tree.py
./delme.temp1.md
./delme.temp2.md
./README.md
./README2.md
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

```

Descripción:
•	Tipos de archivos (-type)
•	Nombres con patrones (-name)
•	Lógica booleana (-o, paréntesis)
•	Control del recorrido (-prune)
•	Mostrar resultado (-print)

PARTE 1: Omisión (PRUNE)
text
-type d \( -name ".git" -o -name ".venv" -o -name "__pycache__" \) -prune
    -type d: Busca directorios (no archivos)
    \( ... \): Agrupa condiciones (los paréntesis deben escaparse con \)
    -name ".git" -o: Nombre exacto ".git" OR (la -o significa OR)
    -name ".venv" -o: Nombre ".venv" OR
    -name "__pycache__": Nombre "pycache"
    -prune: NO DESCENDER en estos directorios (los omite del recorrido)
PARTE 2: CONEXIÓN LÓGICA
text
-o
    La -o (OR) conecta la primera parte con la segunda
    Lógica completa: "Si es un directorio a excluir, poda (-prune) O busca los archivos que siguen"
PARTE 3: INCLUSIÓN (PRINT)
text
-type f \( -name "*.py" -o -name "*.md" -o -name "manage.py" -o -name "requirements.txt" -o -name "db.sqlite3" \) -print
    -type f: Busca archivos regulares (no directorios, enlaces, etc.)
    \( ... \): Otro grupo de condiciones
    -name "*.py" -o: Archivos que terminen en .py OR
    -name "*.md" -o: Archivos .md OR
    etc... para los otros tipos de archivos
    -print: Imprime los resultados (implícito en algunos find, pero explícito aquí)

Aunque se podría incluir en la macro el comando find considero que es necesario establecer como punto de control la creación, edición, ordenación y supervisión de Lista.txt.
Para editar Lista.txt he empleado Notepad++.

Se puede pasar Lista.txt una vez editada a una IA para generar una estructura de tipo árbol.
DeepSeek me ha dado el siguiente script de Python.

```Bash
colorful_tree.py
```

```Python
#!/usr/bin/env python3
# colorful_tree.py

import os

class TreeGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.paths = []
        self.tree = {}
        
    def load_paths(self):
        """Carga las rutas del archivo"""
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.paths = [line.strip() for line in f if line.strip()]
    
    def build_tree(self):
        """Construye la estructura del árbol"""
        for path in self.paths:
            # Remover ./ inicial
            clean_path = path[2:] if path.startswith('./') else path
            parts = clean_path.split('/')
            
            current = self.tree
            for part in parts:
                if part not in current:
                    current[part] = {}
                current = current[part]
    
    def print_colored_tree(self, node=None, indent="", is_last=True):
        """Imprime el árbol con colores"""
        if node is None:
            node = self.tree
        
        items = list(node.items())
        
        for i, (name, children) in enumerate(items):
            is_last_item = (i == len(items) - 1)
            
            # Determinar el símbolo y color
            if not children:  # Es un archivo
                if name.endswith('.py'):
                    symbol = "📄"
                    color = "\033[92m"  # Verde
                elif name.endswith('.txt'):
                    symbol = "📝"
                    color = "\033[93m"  # Amarillo
                elif name == '__init__.py':
                    symbol = "🧩"
                    color = "\033[96m"  # Cian
                elif name == 'manage.py':
                    symbol = "⚙️"
                    color = "\033[95m"  # Magenta
                else:
                    symbol = "📄"
                    color = "\033[90m"  # Gris
                reset = "\033[0m"
            else:  # Es un directorio
                symbol = "📁"
                color = "\033[94m"  # Azul
                reset = "\033[0m"
            
            # Imprimir con formato
            connector = "└── " if is_last_item else "├── "
            print(f"{indent}{connector}{color}{symbol} {name}{reset}")
            
            # Llamada recursiva para hijos
            new_indent = indent + ("    " if is_last_item else "│   ")
            self.print_colored_tree(children, new_indent, is_last_item)
    
    def run(self):
        """Ejecuta el generador completo"""
        print("\033[1m🌳 ESTRUCTURA DEL PROYECTO DJANGO\033[0m")
        print("\033[90m" + "═" * 50 + "\033[0m")
        
        self.load_paths()
        self.build_tree()
        self.print_colored_tree()
        
        # Estadísticas
        print("\n\033[90m" + "═" * 50 + "\033[0m")
        print("\033[1m📊 ESTADÍSTICAS:\033[0m")
        print(f"  Total de rutas: {len(self.paths)}")
        
        # Análisis de la estructura Django
        print("\n\033[1m🏗️  ESTRUCTURA DJANGO:\033[0m")
        print("  • Aplicación 'scraper': Sí ✓")
        print("  • Archivo manage.py: Sí ✓")
        print("  • Settings Django: Sí ✓")
        print("  • Models.py: Sí ✓")
        print("  • Migraciones: Sí ✓")

if __name__ == "__main__":
    generator = TreeGenerator("Lista.txt")
    generator.run()
```

Que da como resultado:

```Bash
Coder@F5-LAPMAD-124 MINGW64 ~/Proyectos/webscraper (develop)
$ python ./colorful_tree.py
🌳 ESTRUCTURA DEL PROYECTO DJANGO
══════════════════════════════════════════════════
├── 📝 requirements.txt
└── 📁 webscraper_project
    ├── 📄 manage.py
    ├── 📁 scraper
    │   ├── 📄 __init__.py
    │   ├── 📄 admin.py
    │   ├── 📄 apps.py
    │   ├── 📁 management
    │   │   ├── 📄 __init__.py
    │   │   └── 📁 commands
    │   │       ├── 📄 __init__.py
    │   │       └── 📄 scraper.py
    │   ├── 📁 migrations
    │   │   ├── 📄 0001_initial.py
    │   │   └── 📄 __init__.py
    │   ├── 📄 models.py
    │   ├── 📁 services
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 scrape.py
    │   │   ├── 📄 scrape_ChatGPT_Corregido.py
    │   │   └── 📄 scrape_inline.py
    │   ├── 📄 tests.py
    │   └── 📄 views.py
    └── 📁 webscraper_project
        ├── 📄 __init__.py
        ├── 📄 asgi.py
        ├── 📄 settings.py
        ├── 📄 urls.py
        └── 📄 wsgi.py

══════════════════════════════════════════════════
📊 ESTADÍSTICAS:
  Total de rutas: 22

🏗️  ESTRUCTURA DJANGO:
  • Aplicación 'scraper': Sí ✓
  • Archivo manage.py: Sí ✓
  • Settings Django: Sí ✓
  • Models.py: Sí ✓
  • Migraciones: Sí ✓
```

Si se ejecuta ./bucle5.sh desde la ruta en la que se ha generado Lista.txt, se obtienen dos archivos .md que he pasado a pdf usando obsidian.

```Bash
bucle5.sh
```

```Bash
#!/bin/bash
# Inicializa o vacía el archivo intermedio para evitar acumular datos de ejecuciones previas
> delme.temp1.md
# Itera sobre cada línea (archivo) definida en el índice Lista.txt
for archivo in $(cat Lista.txt)
do
	{
		# Extrae la cadena después del último punto para identificar el lenguaje
		extension="${archivo##*.}"
		
		# Imprime el encabezado del archivo como un título de nivel 4 en Markdown
		echo ""
		echo "#### \`$archivo\`"
		echo ""
		
		# Crea un bloque informativo para mostrar la ruta relativa del archivo
		echo "\`\`\`Path"
		echo "$archivo"
		echo "\`\`\`"
		echo ""
		# Estructura condicional para asignar el resaltado de sintaxis adecuado
		if [ "$extension" == "py" ]; then
			echo "\`\`\`python"
			cat "$archivo"   # Vuelca el contenido del script Python
		elif [ "$extension" == "js" ]; then
			echo "\`\`\`javascript"
			cat "$archivo"   # Vuelca el contenido del archivo JavaScript
		elif [ "$extension" == "css" ]; then
			echo "\`\`\`css"
			cat "$archivo"   # Vuelca el contenido del archivo CSS
		elif [ "$extension" == "html" ]; then
			echo "\`\`\`html"
			cat "$archivo"   # Vuelca el contenido del archivo HTML
		elif [ "$extension" == "md" ]; then
			echo "\`\`\`markdown"
			cat "$archivo"   # Vuelca el contenido del archivo Markdown
		elif [ "$extension" == "txt" ]; then
			echo "\`\`\`text"
			cat "$archivo"   # Vuelca el contenido del archivo de texto plano
		elif [ "$extension" == "example" ]; then
			echo "\`\`\`text"
			cat "$archivo"   # Archivos de ejemplo (.env.example, etc.)
		elif [ "$extension" == "gitignore" ]; then
			echo "\`\`\`gitignore"
			cat "$archivo"   # Archivo .gitignore
		# elif [ "$extension" == "png" ]; then
			# echo "[Imagen PNG omitida]"
			# echo "(archivo binario: $archivo)"
		# elif [ "$extension" == "webp" ]; then
			# echo "[Imagen WEBP omitida]"
			# echo "(archivo binario: $archivo)"
		else
			echo "\`\`\`text"
			cat "$archivo"   # Extensión desconocida o no contemplada
		fi
		# Cierra el bloque de código Markdown y añade espaciado
		echo ""
		echo "\`\`\`"
		echo ""
		echo "<div style=\"page-break-after: always;\"></div>"
		echo ""
	} >> delme.temp1.md # Redirige toda la salida del bloque al archivo temporal
done
# PROCESAMIENTO FINAL:
# 1. sed: Normaliza todos los finales de línea al estándar Windows (\r\n)
# 2. perl: Busca el cierre de bloque seguido de 3 saltos de línea y lo reduce a 1 salto
sed 's/\r$//; s/$/\r/' delme.temp1.md | \
perl -0777 -pe 's/\`\`\`\r\n\r\n\r\n/\`\`\`\r\n/g' > \
delme.temp2.md
echo "Proceso finalizado: delme.temp2.md generado."
```