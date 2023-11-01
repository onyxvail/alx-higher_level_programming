const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=jsons';
window.$.get(apiUrl, function (data) {
  window.$('#character').text(data.name);
});
