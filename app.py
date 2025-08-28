from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

story = {
    "start": {
        "text": "คุณตื่นขึ้นมาในป่าลึกลับ มีสองทางให้เลือก",
        "choices": {
            "เดินไปทางซ้าย": "river",
            "เดินไปทางขวา": "cave"
        }
    },
    "river": {
        "text": "คุณเจอแม่น้ำไหลเชี่ยว จะทำอย่างไร?",
        "choices": {
            "ข้ามแม่น้ำ": "drown",
            "เดินเลียบแม่น้ำ": "village"
        }
    },
    "cave": {
        "text": "คุณเข้าไปในถ้ำและพบสัตว์ประหลาด!",
        "choices": {
            "สู้มัน": "fight",
            "วิ่งหนี": "start"
        }
    },
    "drown": {
        "text": "คุณพยายามข้ามแม่น้ำ แต่จมน้ำเสียชีวิต...",
        "choices": {
            "เริ่มใหม่": "start"
        }
    },
    "village": {
        "text": "คุณเดินมาจนถึงหมู่บ้านและได้รับการช่วยเหลือ ชนะแล้ว!",
        "choices": {
            "เล่นอีกครั้ง": "start"
        }
    },
    "fight": {
        "text": "คุณสู้และเอาชนะสัตว์ประหลาดได้! พบสมบัติในถ้ำ!",
        "choices": {
            "เริ่มใหม่": "start"
        }
    }
}


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/game/<scene>')
def game(scene):
    data = story.get(scene)
    if not data:
        return redirect(url_for('index'))
    return render_template("game.html", scene=scene, text=data["text"], choices=data["choices"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
