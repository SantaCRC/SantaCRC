import json
import os
from datetime import datetime

import feedparser
import requests

session = requests.Session()
session.headers.update({
    "User-Agent": "MyReadmeBot/1.0",
    "X-Readme-Key": os.getenv("README_ACCESS_TOKEN", "")
})

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

</div>
"""

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not OPENWEATHER_API_KEY:
    raise EnvironmentError("OPENWEATHER_API_KEY environment variable is not set.")

city = "Ferrol"
weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"

weather_section = """<div align="center">

## Weather information not available at the moment.

</div>
"""

try:
    weather_response = session.get(weather_url, timeout=10)
    weather_response.raise_for_status()
    weather_data = weather_response.json()
    weather_description = weather_data["weather"][0]["description"].capitalize()
    temperature = weather_data["main"]["temp"]

    weather_section = f"""<div align="center">

## Weather in {city}

Current temperature: **{temperature}°C**

Weather description: **{weather_description}**

</div>
"""
except Exception as e:
    print(f"[WARN] Weather request failed: {e}")

instagram_section = """<div align="center">

## Latest Instagram Posts

</div>

"""

try:
    instagram_file = "private-data/static/instagram.json"

    with open(instagram_file, "r", encoding="utf-8") as f:
        instagram_data = json.load(f)

    latest_posts = instagram_data[:9]

    cols = 3
    rows = (len(latest_posts) + cols - 1) // cols

    instagram_section += "|  |  |  |\n"
    instagram_section += "|---|---|---|\n"

    for r_idx in range(rows):
        row_cells = []
        for c in range(cols):
            idx = r_idx * cols + c
            if idx < len(latest_posts):
                post = latest_posts[idx]
                image_url = post.get("image_url") or post.get("image") or ""
                post_link = post.get("source_link") or post.get("link") or "#"
                caption = post.get("caption", "").strip().replace("\n", " ")
                if len(caption) > 80:
                    caption = caption[:77] + "..."
                alt = caption or "Instagram image"

                if image_url:
                    cell = f'[![{alt}]({image_url} "{alt}")]({post_link})'
                else:
                    cell = f'[Link]({post_link})'
            else:
                cell = ""

            row_cells.append(cell)

        instagram_section += "| " + " | ".join(row_cells) + " |\n"

    instagram_section += "\n"
except Exception as e:
    print(f"[WARN] Instagram file read failed: {e}")
    instagram_section = """<div align="center">

## Instagram posts could not be retrieved.

</div>
"""

rss_feed_url = "https://fabianalvarez.dev/index.xml"
rss_feed = feedparser.parse(
    rss_feed_url,
    agent="MyReadmeBot/1.0",
    request_headers={
        "X-Readme-Key": os.getenv("README_ACCESS_TOKEN", "")
    }
)

blog_section = """<div align="center">

## Latest Blog Posts

</div>

"""

if rss_feed.bozo:
    blog_section += "<div align=\"center\">⚠️ Failed to load blog posts.</div>\n"
else:
    sorted_entries = sorted(
        rss_feed.entries,
        key=lambda entry: entry.get("published_parsed") or entry.get("updated_parsed") or datetime.min.timetuple(),
        reverse=True
    )

    blog_section += "<div align=\"center\">\n\n"

    for entry in sorted_entries[:3]:
        if entry.get("published_parsed"):
            pub_date = datetime(*entry.published_parsed[:6]).strftime("%d %b %Y")
        elif entry.get("updated_parsed"):
            pub_date = datetime(*entry.updated_parsed[:6]).strftime("%d %b %Y")
        else:
            pub_date = "Unknown date"

        summary = entry.get("summary", "").strip().replace("\n", " ")
        if len(summary) > 150:
            summary = summary[:147] + "..."

        title = entry.get("title", "Untitled")
        link = entry.get("link", "#")
        blog_section += f"- **[{title}]({link})** ({pub_date}): {summary}\n"

    blog_section += "\n</div>\n"

with open("README.md", "w", encoding="utf-8") as file:
    file.write(README_CONSTANT)
    file.write("\n")
    file.write(weather_section)
    file.write("\n")
    file.write(instagram_section)
    file.write("\n")
    file.write(blog_section)

print("README.md generado con éxito.")
