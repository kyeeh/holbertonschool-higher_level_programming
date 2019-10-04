$(document).ready(function () {
  function greetings () {
    $('DIV#hello').empty();
    const language = $('INPUT#language_code').val();
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + language,
      function (data) {
        $('DIV#hello').append(data.hello);
      }
    );
  }
  $('INPUT#btn_translate').click(function () {
    greetings();
  });
  $('INPUT#language_code').keypress(function (k) {
    const key = k.which;
    if (key === 13) {
      greetings();
    }
  });
});
