(() => {
  const game = document.querySelector('[data-code-breaker]');
  if (!game) return;

  const form = game.querySelector('#code-breaker-form');
  const input = game.querySelector('#code-breaker-guess');
  const help = game.querySelector('#code-breaker-help');
  const status = game.querySelector('[data-code-breaker-status]');
  const history = game.querySelector('[data-code-breaker-history]');
  const reset = game.querySelector('[data-code-breaker-reset]');
  const maxAttempts = 8;
  let secret = createSecret();
  let attempts = 0;
  let finished = false;

  function createSecret() {
    return String(Math.floor(1000 + Math.random() * 9000));
  }

  function scoreGuess(guess) {
    let exact = 0;
    const secretRest = [];
    const guessRest = [];

    for (let index = 0; index < secret.length; index += 1) {
      if (guess[index] === secret[index]) {
        exact += 1;
      } else {
        secretRest.push(secret[index]);
        guessRest.push(guess[index]);
      }
    }

    let misplaced = 0;
    for (const digit of guessRest) {
      const matchIndex = secretRest.indexOf(digit);
      if (matchIndex !== -1) {
        misplaced += 1;
        secretRest.splice(matchIndex, 1);
      }
    }

    return { exact, misplaced };
  }

  function updateHelp() {
    const remaining = maxAttempts - attempts;
    help.textContent = `Use exactly four digits. You have ${remaining} attempts remaining.`;
  }

  function addHistory(guess, exact, misplaced) {
    const item = document.createElement('li');
    item.textContent = `${guess}: ${exact} exact, ${misplaced} misplaced`;
    history.prepend(item);
  }

  function setFinished(message) {
    finished = true;
    input.disabled = true;
    form.querySelector('button[type="submit"]').disabled = true;
    status.textContent = message;
  }

  function restart() {
    secret = createSecret();
    attempts = 0;
    finished = false;
    history.replaceChildren();
    input.disabled = false;
    form.querySelector('button[type="submit"]').disabled = false;
    input.value = '';
    status.textContent = 'New code generated. 8 attempts remaining.';
    updateHelp();
    input.focus();
  }

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (finished) return;

    const guess = input.value.trim();
    if (!/^\d{4}$/.test(guess)) {
      status.textContent = 'Enter exactly four digits before submitting.';
      input.focus();
      return;
    }

    attempts += 1;
    const { exact, misplaced } = scoreGuess(guess);
    addHistory(guess, exact, misplaced);
    input.value = '';
    updateHelp();

    if (exact === 4) {
      setFinished(`Access granted in ${attempts} attempt${attempts === 1 ? '' : 's'}.`);
      return;
    }

    const remaining = maxAttempts - attempts;
    if (remaining === 0) {
      setFinished(`Access denied. The code was ${secret}. Reset to try a new code.`);
      return;
    }

    status.textContent = `${exact} exact, ${misplaced} misplaced. ${remaining} attempts remaining.`;
    input.focus();
  });

  reset.addEventListener('click', restart);
})();
