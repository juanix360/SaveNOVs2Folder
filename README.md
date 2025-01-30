📂 Organizador de Archivos LiDAR

📄 Descripción

Este script en Python automatiza la organización de archivos .novb en un entorno de datos LiDAR. Escanea el directorio base en busca de archivos sessionMetadata.json, extrae el nombre del archivo .novb asociado y lo mueve a la carpeta correspondiente.

🚀 Características

✅ Escaneo automático de un directorio base en busca de archivos sessionMetadata.json.
✅ Extracción del nombre del archivo .novb desde la clave collectionSystemTrajectoryName.
✅ Copia automática del archivo .novb a la carpeta donde se encuentra el archivo JSON correspondiente.
✅ Prevención de duplicados, verificando si el archivo ya existe en la carpeta destino.

🔧 Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

🐍 Python 3.x

📦 Pandas

Instálalas con:

pip install pandas

🛠 Uso

1️⃣ Modifica la variable normalized_path en el script para que apunte al directorio base donde se encuentran los datos LiDAR.
2️⃣ Ejecuta el script con:

python script.py

👤 Autor

📌 Juan Ortiz

📝 Licencia

Este proyecto se distribuye bajo la licencia MIT.
