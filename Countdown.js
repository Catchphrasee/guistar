
window.onload = function() {
    var gameCountdown = document.querySelector('#game-countdown');
    setTimeout( function(){
         gameCountdown.innerHTML = "3";
      },0100);
    
    setTimeout( function(){
       gameCountdown.innerHTML = "2";
    },1100);
    
    setTimeout( function(){
       gameCountdown.innerHTML = "1";
    },2100);  
    
    setTimeout( function(){
       gameCountdown.innerHTML = "Go";
    },3100);  
    
    setTimeout( function(){
       gameCountdown.innerHTML = "";
    },4100);  
  };