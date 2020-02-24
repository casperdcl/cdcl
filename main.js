$(function(){
  $('div.gist').each(function(){
    const gist = $(this);
    const URL = "https://api.github.com/gists/" + gist.text();
    function update(){
      $.get(URL, function(data){
        const content = Object.values(data.files)[0].content;
        gist.html(content.split("\n").join("<br/>"));
      });
    }
    update();
    setInterval(update, 1000 * 60);
  });
});
