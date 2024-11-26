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

# Generar la tabla Markdown sin encabezado, con imágenes como enlaces
markdown_table = '## Latest Instagram Posts\n\n'
markdown_table += '|---|---|---|\n'

# Recolectar las URLs de las imágenes y enlaces de las publicaciones
image_links = [
    (post.get('image', ''), post.get('link', '#')) for post in latest_posts
]

# Añadir las imágenes con enlaces a la tabla
markdown_table += '|'
for image_url, post_link in image_links:
    markdown_table += f' [![]({image_url})]({post_link}) |'
markdown_table += '\n'

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
