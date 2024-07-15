from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Definir símbolos, suas probabilidades e pagamentos
symbols = ["🍉", "🍒", "🍋", "⭐", "🔔", "7️⃣"]
probabilities = [0.3, 0.25, 0.2, 0.15, 0.07, 0.03]  # Probabilidades devem somar 1
payouts_2 = {
    "🍉": 0.20,
    "🍒": 0.35,
    "🍋": 0.45,
    "⭐": 0.75,
    "🔔": 1.75,
    "7️⃣": 3.25
}
payouts_3 = {
    "🍉": 1.40,
    "🍒": 1.70,
    "🍋": 2.25,
    "⭐": 4.50,
    "🔔": 8.50,
    "7️⃣": 20.00
}

# Função para selecionar um símbolo com base nas probabilidades
def get_symbol():
    return random.choices(symbols, probabilities)[0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin', methods=['POST'])
def spin():
    data = request.json
    balance = round(data['balance'], 2)
    spin_value = round(data['spinValue'], 2)

    results = [[get_symbol() for _ in range(3)] for _ in range(3)]

    win_amount = 0
    winning_lines = []

    # Check horizontal lines
    for i, row in enumerate(results):
        if row[0] == row[1] == row[2]:
            win_amount += spin_value * payouts_3[row[0]]
            winning_lines.append(f'row{i+1}')
        elif row[0] == row[1]:
            win_amount += spin_value * payouts_2[row[0]]

    # Check diagonals
    if results[0][0] == results[1][1] == results[2][2]:
        win_amount += spin_value * payouts_3[results[1][1]]
        winning_lines.append('diag1')
    if results[0][2] == results[1][1] == results[2][0]:
        win_amount += spin_value * payouts_3[results[1][1]]
        winning_lines.append('diag2')

    if win_amount > 0:
        balance += round(win_amount, 2)
        message = f"You Win! Total Win: ${win_amount:.2f}"
    else:
        balance -= round(spin_value, 2)
        message = "Try Again!"

    return jsonify({
        'results': results,
        'balance': round(balance, 2),
        'message': message,
        'winningLines': winning_lines
    })

if __name__ == '__main__':
    app.run(debug=True)
