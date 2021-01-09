$(document).ready(function(){
    $('#notification').click(function(){
      $('.toast').toast({delay: 2000});
      $('.toast').toast('show');
    });
  });