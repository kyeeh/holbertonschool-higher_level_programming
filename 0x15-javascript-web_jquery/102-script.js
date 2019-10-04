$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const language = $('INPUT#language_code').val();
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + language,
      function (data) {
        $('DIV#hello').append(data.hello);
      }
    );
  });
});
