import tkinter as tk
import random

# Inicializa o saldo e o valor do giro
balance = 100
spin_value = 10

# Função para girar os rolos
def spin():
    global balance
    symbols = ["🍒", "🔔", "🍋", "⭐", "🍉", "7️⃣"]
    result1 = random.choice(symbols)
    result2 = random.choice(symbols)
    result3 = random.choice(symbols)

    reel1.config(text=result1)
    reel2.config(text=result2)
    reel3.config(text=result3)

    if result1 == result2 == result3:
        balance += spin_value * 10
        result_label.config(text="Jackpot!")
    else:
        balance -= spin_value
        result_label.config(text="Try Again!")

    balance_label.config(text=f"Balance: ${balance}")

# Função para atualizar o valor do giro
def update_spin_value(value):
    global spin_value
    spin_value = int(value)

# Configuração da janela principal
root = tk.Tk()
root.title("Slot Machine")
root.configure(bg="#2c3e50")

# Container principal
container = tk.Frame(root, bg="#2c3e50")
container.pack(expand=True)

# Máquina caça-níqueis
slot_machine = tk.Frame(container, bg="#2c3e50")
slot_machine.pack(pady=20)

reel1 = tk.Label(slot_machine, text="🍒", font=("Arial", 50), bg="#34495e", fg="#ecf0f1", width=3, height=2)
reel1.pack(side=tk.LEFT, padx=10)

reel2 = tk.Label(slot_machine, text="🍒", font=("Arial", 50), bg="#34495e", fg="#ecf0f1", width=3, height=2)
reel2.pack(side=tk.LEFT, padx=10)

reel3 = tk.Label(slot_machine, text="🍒", font=("Arial", 50), bg="#34495e", fg="#ecf0f1", width=3, height=2)
reel3.pack(side=tk.LEFT, padx=10)

# Botão de girar
spin_button = tk.Button(container, text="Spin", font=("Arial", 20), bg="#e74c3c", fg="white", command=spin)
spin_button.pack(pady=10)

# Campo para exibir o saldo
balance_label = tk.Label(container, text=f"Balance: ${balance}", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
balance_label.pack()

# Campo para alterar o valor do giro
spin_value_label = tk.Label(container, text="Spin Value:", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
spin_value_label.pack(pady=(10, 0))

spin_value_entry = tk.Entry(container, font=("Arial", 20), bg="#34495e", fg="#ecf0f1")
spin_value_entry.pack()
spin_value_entry.insert(0, spin_value)

# Botão para atualizar o valor do giro
update_button = tk.Button(container, text="Update Spin Value", font=("Arial", 20), bg="#3498db", fg="white", command=lambda: update_spin_value(spin_value_entry.get()))
update_button.pack(pady=10)

# Resultado
result_label = tk.Label(container, text="", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
result_label.pack()

# Inicia a aplicação
root.mainloop()
