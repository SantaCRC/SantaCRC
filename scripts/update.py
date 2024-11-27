import requests

# Parte constante del README
README_CONSTANT = """<div align="center">
  
## About me
  
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&center=true&multiline=true&width=420&height=100&lines=Hi!+my+name+is+Fabian;I+am+mechatronics+engineer;from+Costa+Rica)](https://github.com/SantaCRC)

### Programming languages
  ![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)
  ![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=c-sharp&logoColor=white)
![Dart](https://img.shields.io/badge/dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Octave](https://img.shields.io/badge/OCTAVE-darkblue?style=for-the-badge&logo=octave&logoColor=fcd683)
  ![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white)
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

  ### Frameworks
  ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
  ![Angular](https://img.shields.io/badge/angular-%23DD0031.svg?style=for-the-badge&logo=angular&logoColor=white)
  ![Angular.js](https://img.shields.io/badge/angular.js-%23E23237.svg?style=for-the-badge&logo=angularjs&logoColor=white)
  ![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
  ![Expo](https://img.shields.io/badge/expo-1C1E24?style=for-the-badge&logo=expo&logoColor=#D04A37)
  ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white)
  ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Threejs](https://img.shields.io/badge/threejs-black?style=for-the-badge&logo=three.js&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
  ![Tensor](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white)
  
  ### Social
  [![Website](https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://fabianalvarez.dev)
    [![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/fabian-a-alvarez/)
   [![twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/_SantaCRC_)

## Stats
[![GitHub Streak](http://github-readme-streak-stats.herokuapp.com?user=SantaCRC&theme=buefy-dark&hide_border=true&date_format=M%20j%5B%2C%20Y%5D&background=DD272700)](https://github.com/SantaCRC)
  
  [![trophy](https://github-profile-trophy.vercel.app/?username=santacrc&theme=discord&no-bg=true&no-frame=true&rank=SECRET,SSS,SS,S,AAA,AA,A,B,C&column=3)](https://github.com/SantaCRC)
"""

# API de OpenWeather
OPENWEATHER_API_KEY = "279efc54469dc86932b9bf4bd544516f"
city = "Ferrol"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"

# Obtener datos del clima
weather_response = requests.get(weather_url)
if weather_response.status_code == 200:
    weather_data = weather_response.json()
    weather_description = weather_data["weather"][0]["description"].capitalize()
    temperature = weather_data["main"]["temp"]
    weather_section = f"## Weather in {city}\n\nCurrent temperature: **{temperature}°C**\n\nWeather description: **{weather_description}**\n\n"
else:
    weather_section = "## Weather information not available at the moment.\n\n"

# API de Instagram JSON
instagram_url = 'https://fabianalvarez.dev/instagram.json'

# Obtener las últimas publicaciones de Instagram
instagram_response = requests.get(instagram_url)
if instagram_response.status_code == 200:
    instagram_data = instagram_response.json()
    latest_posts = instagram_data[:3]

    instagram_section = '## Latest Instagram Posts\n\n|---|---|---|\n|'
    for post in latest_posts:
        image_url = post.get('image', '')
        post_link = post.get('link', '#')
        instagram_section += f' [![]({image_url})]({post_link}) |'
    instagram_section += '\n'
else:
    instagram_section = "## Instagram posts could not be retrieved.\n\n"

# Crear el archivo README.md
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(README_CONSTANT)
    file.write('\n')
    file.write(weather_section)
    file.write('\n')
    file.write(instagram_section)

print("README.md generado con éxito.")
