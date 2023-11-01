const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
window.$.get(apiUrl, function (data) {
  window.$('#hello').text(data.hello);
});
