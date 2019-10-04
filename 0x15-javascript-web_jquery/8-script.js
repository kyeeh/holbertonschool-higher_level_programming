$.getJSON('https://swapi.co/api/films/?format=json',
  function (data) {
    $.each(data.movies, function (index, movie) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
