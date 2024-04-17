document.getElementById('translate-button').addEventListener('click', function() {
  var englishText = document.getElementById('english-text').value;
  var file = document.getElementById('file-upload').files[0];

  var formData = new FormData();
  formData.append('englishText', englishText);
  formData.append('file', file);

  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/translate');
  xhr.onload = function() {
    if (xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      document.getElementById('translated-text').value = response.translatedText;
      document.getElementById('output-link').innerHTML =
        '<a href="' + response.outputFile + '">Download Translated PDF</a>';
    } else {
      console.log('Error:', xhr.status);
    }
  };
  xhr.send(formData);
});
