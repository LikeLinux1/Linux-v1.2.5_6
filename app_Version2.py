import random
from flask import Flask, render_template_string

app = Flask(__name__)

themes = [
    {"title": "Добро пожаловать!", "desc": "Это ваш новый сайт в стиле 90-х!"},
    {"title": "Гостевая книга", "desc": "Оставьте свой комментарий ниже."},
    {"title": "Домашняя страница", "desc": "Вы нашли самую олдскульную страницу!"},
    {"title": "Старый блог", "desc": "Этот блог написан в стиле Windows 98."},
]

backgrounds = [
    "https://www.transparenttextures.com/patterns/old-wall.png",
    "https://www.transparenttextures.com/patterns/diamond-upholstery.png",
    "https://www.transparenttextures.com/patterns/brick-wall.png",
    "https://www.transparenttextures.com/patterns/arches.png",
]

fonts = [
    "Comic Sans MS, cursive, sans-serif",
    "Courier New, monospace",
    "Times New Roman, serif",
    "Verdana, Geneva, sans-serif",
]

@app.route("/")
def index():
    theme = random.choice(themes)
    bg = random.choice(backgrounds)
    font = random.choice(fonts)
    html = f"""
    <html>
    <head>
        <title>{theme['title']}</title>
        <meta charset="utf-8"/>
        <style>
            body {{
                background-image: url('{bg}');
                background-color: #e0e0e0;
                font-family: {font};
                color: #222;
                margin: 0;
                padding: 0;
            }}
            .container {{
                background: #fff9e3cc;
                border: 3px double #0000aa;
                margin: 40px auto;
                width: 80%;
                max-width: 600px;
                box-shadow: 5px 5px 0 #0000aa;
                padding: 25px;
                text-align: center;
            }}
            h1 {{
                text-shadow: 1px 1px 0 #fff, 2px 2px 0 #000;
                color: #0000aa;
                font-size: 2.2em;
                margin-bottom: 15px;
            }}
            .marquee {{
                width: 100%;
                background: #ff0;
                color: #d00;
                font-weight: bold;
                padding: 5px 0;
                margin-bottom: 20px;
                font-size: 1.2em;
                border-top: 2px dashed #d00;
                border-bottom: 2px dashed #d00;
            }}
            .blink {{
                animation: blink 1s linear infinite;
            }}
            @keyframes blink {{
                0% {{ opacity: 1; }}
                50% {{ opacity: 0; }}
                100% {{ opacity: 1; }}
            }}
            footer {{
                margin-top: 45px;
                font-size: 0.9em;
                color: #999;
                border-top: 1px dotted #000;
                padding-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="marquee"><span class="blink">Сайт сгенерирован автоматически!</span></div>
            <h1>{theme['title']}</h1>
            <p>{theme['desc']}</p>
            <img src="https://www.gifgratis.net/archivos/old_computer.gif" width="120" alt="Oldschool Computer"/>
            <footer>Copyright © 1999-{2025} | Сайт-рандомайзер</footer>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)