import requests
import re

# URL del archivo JSON de Instagram
url = 'https://fabianalvarez.dev/instagram.json'

# Obtener los datos del JSON
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print("No se pudo obtener el archivo JSON.")
    exit()

# Extraer las tres últimas publicaciones
latest_posts = data[:3]

# Generar la tabla Markdown sin encabezado
markdown_table = '## Latest Instagram Posts\n\n'

# Recolectar las URLs de las imágenes
image_urls = [post.get('image', '') for post in latest_posts]

# Añadir las imágenes a la tabla
markdown_table += '|'
for url in image_urls:
    markdown_table += f' ![]({url}) |'
markdown_table += '\n'

markdown_table += '|---|---|---|\n'
# Leer el archivo README.md
with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

# Reemplazar la sección existente
updated_content = re.sub(
    r'## Latest Instagram Posts\n\n.*?\n\n',
    markdown_table + '\n',
    readme_content,
    flags=re.DOTALL
)

# Escribir el contenido actualizado en README.md
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(updated_content)

print('La sección "## Latest Instagram Posts" ha sido actualizada con éxito.')
