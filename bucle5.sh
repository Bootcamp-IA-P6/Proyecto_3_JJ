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