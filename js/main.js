$(function(){
  $('div.gist').each(function(){
    var gist = $(this);
    $.get("https://api.github.com/gists/" + gist.text(), function(data){
      $.each(data.files, function(name, file){
        gist.html(file.content.split("\n").join("<br/>"));
      });
    });
  });
});
