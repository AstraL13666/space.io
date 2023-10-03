function loadReadme(filename) {
  fetch(filename)
    .then(response => response.text())
    .then(text => {
      const container = document.getElementById('readme-container');
      container.innerHTML = text;
    });
}
