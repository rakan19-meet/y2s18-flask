from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    players_list=["Lebron", "Kyrie", "Kobe", "James Harden"]
    for i in players_list[]:
        print(i)
    return render_template(
        "index.html")

if __name__ == '__main__':
   app.run(debug = True)