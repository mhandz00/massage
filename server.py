from flask import Flask, render_template
import threading
import turtle
import time

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("massage_by_py.html")  # تحميل صفحة HTML عند فتح الرابط

# دالة لرسم الشكل باستخدام Turtle
def draw():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    turtle.speed(2)  # جعل الرسم تدريجيًا
    
    def draw_rectangle(x, y, width, height, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(width)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
        turtle.end_fill()
    
    def draw_candle(x, y, height):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor("black")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(10)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
        turtle.end_fill()
    
    def draw_flame(x, y):
        turtle.penup()
        turtle.goto(x + 5, y + 5)
        turtle.pendown()
        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
    
    def draw_heart(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("red")
        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.left(140)
        turtle.forward(113)
        for _ in range(200):
            turtle.right(1)
            turtle.forward(1)
        turtle.left(120)
        for _ in range(200):
            turtle.right(1)
            turtle.forward(1)
        turtle.forward(113)
        turtle.end_fill()
    
    def show_message(x, y, message, color="black"):
        turtle.penup()
        turtle.goto(x, y)
        turtle.color(color)
        turtle.write(message, align="center", font=("Arial", 16, "bold"))
    
    # رسم التورتة بالتدريج
    draw_rectangle(-50, -100, 100, 40, "pink")
    time.sleep(0.5)
    draw_rectangle(-40, -60, 80, 40, "pink")
    time.sleep(0.5)
    draw_rectangle(-30, -20, 60, 40, "pink")
    time.sleep(0.5)
    
    # رسم الشموع بالتدريج
    draw_candle(-20, 20, 40)
    time.sleep(0.5)
    draw_candle(20, 20, 40)
    time.sleep(0.5)
    
    # رسم اللهب
    draw_flame(-20, 60)
    time.sleep(0.5)
    draw_flame(20, 60)
    time.sleep(0.5)
    
    # رسم القلب فوق التورتة
    draw_heart(0, 150)
    time.sleep(0.5)
    
    # كتابة "H" داخل القلب
    show_message(0, 180, "H", "white")
    
    # عرض رسالة تحت القلب
    show_message(0, 90, "Enjoy the sweet moments!", "black")
    
    turtle.done()

# تشغيل الرسم في Thread منفصل حتى لا يتعطل السيرفر
def start_drawing():
    thread = threading.Thread(target=draw)
    thread.start()

if _name_ == "_main_":
    start_drawing()  # تشغيل الرسم تلقائيًا
    app.run(host="0.0.0.0", port=5000, debug=True)