var sounds = {
    w: "sounds/tom-1.mp3",
    a: "sounds/tom-2.mp3",
    s: "sounds/tom-3.mp3",
    d: "sounds/tom-4.mp3",
    j: "sounds/snare.mp3",
    k: "sounds/kick-bass.mp3",
    l: "sounds/crash.mp3"
  }
   
  for (i=0; i<document.querySelectorAll(".drum").length; i++){
    document.querySelectorAll(".drum")[i].addEventListener("click", function(){
      new Audio(sounds[this.textContent]).play();
      });
  }
   
  document.addEventListener("keydown", function(event){
    new Audio(sounds[event.key]).play();
  })