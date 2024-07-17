document.getElementById('spinButton').addEventListener('click', spin);

function spin() {
    const symbols = ["🍒", "🔔", "🍋", "⭐", "🍉", "7️⃣"];
    const reel1 = document.getElementById('reel1');
    const reel2 = document.getElementById('reel2');
    const reel3 = document.getElementById('reel3');
    const result = document.getElementById('result');

    const result1 = symbols[Math.floor(Math.random() * symbols.length)];
    const result2 = symbols[Math.floor(Math.random() * symbols.length)];
    const result3 = symbols[Math.floor(Math.random() * symbols.length)];

    reel1.textContent = result1;
    reel2.textContent = result2;
    reel3.textContent = result3;

    if (result1 === result2 && result2 === result3) {
        result.textContent = "Jackpot!";
    } else {
        result.textContent = "Try Again!";
    }
}
