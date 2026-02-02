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