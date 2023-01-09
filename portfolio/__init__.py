from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Aplicativo de rastreamento de hábitos com Python e MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracker",
        "prod": "https://habit-tracker-wvvz.onrender.com"
    },
    {
        "name": "Aplicativo de rastreamento de finanças pessoais com React",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
    },
    {
        "name": "Documentação da API REST com Postman e Swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
    }
]

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/contact")
def contact():
    return render_template("contact.jinja2")