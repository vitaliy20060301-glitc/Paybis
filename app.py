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
<title>Ethereum Payment via Paybis (No KYC)</title>
<style>
body{font-family:Arial,sans-serif;background:#f3f4f6;margin:0;padding:40px}
.box{max-width:520px;margin:auto;background:white;padding:28px;border-radius:16px;box-shadow:0 8px 30px #0001}
input,button{width:100%;padding:13px;margin-top:10px;box-sizing:border-box;border-radius:9px}
input{border:1px solid #ccc}
button{border:0;background:#111;color:white;cursor:pointer;font-weight:bold}
.wallet{word-break:break-all;background:#f1f1f1;padding:12px;border-radius:8px}
.demo{background:#fff3cd;padding:12px;border-radius:8px;margin-bottom:18px}
label{display:block;margin-top:12px;font-weight:bold}
</style>
</head>
<body>
<div class="box">
<h2>Оплата Ethereum карткою</h2>
<div class="demo"><b>УВАГА:</b> Оплата виконується через сервіс Paybis. Для невеликих сум верифікація документів (KYC) не вимагається.</div>

<p>Ethereum-адреса отримувача:</p>
<div class="wallet">{{ wallet }}</div>

<form method="post">
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
        
        # Параметри для Paybis No-KYC On-Ramp
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