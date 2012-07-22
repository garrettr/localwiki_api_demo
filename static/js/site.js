function searchImages(query) {
  // hide gallery, show loading image
  $('#results').hide();
  $('img.loading').show();

  // build query string
  params = { 'query': query };

  $('#results').load("search?" + $.param(params), function () {
    // hide the loading image
    $('img.loading').hide();
    // show the loaded html
    $('#results').show();

    $('#gallery').galleria({ 
      width: 800, 
      height: 450, 
      transition: 'fade' 
    });
  });
}

$(document).ready(function () {

  // hide loading gif for ajax requests
  $('img.loading').hide();

  $("form").submit(function (){

    /* copy input values into an object */
    var values = {};
    $.each($(this).serializeArray(), function(i, field) {
      values[field.name] = field.value;
    });
    console.log(values.search);
    searchImages(values.search);
    return false; // Don't actually submit the form
  });
  
});
