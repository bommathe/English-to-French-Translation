document.getElementById('translation-form').addEventListener('submit', function (event) {
  event.preventDefault();
  const englishText = document.getElementById('english-text').value;

  fetch('/translate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: 'english-text=' + encodeURIComponent(englishText),
  })
    .then(function (response) {
      return response.text();
    })
    .then(function (translatedText) {
      document.getElementById('translated-text').value = translatedText;
    });
});
