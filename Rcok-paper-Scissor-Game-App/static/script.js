async function playGame(choice) {
    const response = await fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ choice: choice })
    });

    const result = await response.json();
    document.getElementById('result').innerHTML = `
        You chose: ${result.user_choice} <br>
        Computer chose: ${result.computer_choice} <br>
        Result: ${result.result}
    `;
}