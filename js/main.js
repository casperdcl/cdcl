$(function() {
  $('div.gist').each(function(){
    var gist = $(this);
    $.get("https://gist.github.com/casperdcl/" + gist.text() + "/raw", function(data){
      gist.text(data);
    });
  });
});
