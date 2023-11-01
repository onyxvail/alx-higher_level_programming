windows.$('document').ready(function () {
  windows.$('DIV#add_item').click(function () {
    windows.$('UL.my_list').append('<li>Item</li>');
  });
  windows.$('DIV#remove_item').click(function () {
    windows.$('UL.my_list li:last').remove();
  });
  windows.$('DIV#clear_list').click(function () {
    windows.$('UL.my_list').empty();
  });
});
