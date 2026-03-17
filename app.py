from flask import Flask, render_template, request, redirect
import sqlite3
import json
import urllib.parse

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/order", methods=["POST"])
def order():
    name = request.form.get("name")
    phone = request.form.get("phone")
    address = request.form.get("address")
    cart = request.form.get("cart")

    db = get_db()

    db.execute(
        "INSERT INTO orders (name, phone, address, product, quantity, status, delivery_boy) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (name, phone, address, cart, 1, "Pending", "")
    )

    db.commit()

    try:
        cart_dict = json.loads(cart)
    except:
        cart_dict = {}

    prices = {
        "20L Jar": 50,
        "1L Pack (12)": 120,
        "500ml Pack (20)": 140,
        "250ml Pack (30)": 150
    }

    message = "NEW FILTERPANI ORDER\n\n"
    message += f"Name: {name}\n"
    message += f"Phone: {phone}\n"
    message += f"Address: {address}\n\n"
    message += "Order Details:\n"

    total = 0

    for item, qty in cart_dict.items():
        price = prices.get(item, 0) * qty
        total += price
        message += f"{item} x {qty} = ₹{price}\n"

    message += f"\nTotal: ₹{total}"

    encoded_message = urllib.parse.quote(message)

    whatsapp_number = "916263928600"
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"

    return redirect(whatsapp_url)


@app.route("/admin")
def admin():
    db = get_db()

    orders = db.execute("SELECT * FROM orders ORDER BY id DESC").fetchall()
    boys = db.execute("SELECT * FROM delivery_boys").fetchall()

    prices = {
        "20L Jar": 50,
        "1L Pack (12)": 120,
        "500ml Pack (20)": 140,
        "250ml Pack (30)": 150
    }

    formatted_orders = []

    for order in orders:
        try:
            cart = json.loads(order["product"])
        except:
            cart = {}

        cart_items = []
        total = 0

        for item, qty in cart.items():
            price = prices.get(item, 0) * qty
            total += price
            cart_items.append(f"{item} × {qty} = ₹{price}")

        formatted_orders.append({
            "id": order["id"],
            "name": order["name"],
            "phone": order["phone"],
            "address": order["address"],
            "status": order["status"],
            "delivery_boy": order["delivery_boy"],
            "cart_items": cart_items,
            "total": total
        })

    return render_template("admin.html", orders=formatted_orders, boys=boys)


@app.route("/assign/<int:id>/<name>")
def assign(id, name):
    db = get_db()
    db.execute("UPDATE orders SET delivery_boy=? WHERE id=?", (name, id))
    db.commit()
    return redirect("/admin")


@app.route("/delivered/<int:id>")
def delivered(id):
    db = get_db()
    db.execute("UPDATE orders SET status='Delivered' WHERE id=?", (id,))
    db.commit()
    return redirect("/admin")


@app.route("/add_delivery", methods=["POST"])
def add_delivery():
    name = request.form.get("name")

    db = get_db()
    db.execute("INSERT INTO delivery_boys (name) VALUES (?)", (name,))
    db.commit()

    return redirect("/admin")


@app.route("/delivery/<name>")
def delivery_panel(name):
    db = get_db()
    orders = db.execute(
        "SELECT * FROM orders WHERE delivery_boy=? AND status='Pending'",
        (name,)
    ).fetchall()

    return render_template("delivery.html", orders=orders, name=name)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
