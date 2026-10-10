const nameInput = document.getElementById('name');
const moodSelect = document.getElementById('mood');
const generateBtn = document.getElementById('generateBtn');
const messageEl = document.getElementById('message');
const quoteEl = document.getElementById('quote');

async function generateVibe() {
  const payload = {
    name: nameInput.value || 'friend',
    mood: moodSelect.value || 'happy',
  };

  try {
    const response = await fetch('/api/greeting', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    messageEl.textContent = data.message;
    quoteEl.textContent = data.quote;
  } catch (error) {
    messageEl.textContent = 'Something went a little sideways. Try again in a moment.';
    quoteEl.textContent = 'The vibe engine is warming up.';
  }
}

generateBtn.addEventListener('click', generateVibe);
nameInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') generateVibe();
});
