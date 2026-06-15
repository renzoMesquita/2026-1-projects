console.log("JS funcionando!!")

let gamePattern = []
let randomNumber

const buttonColour = ["red", "blue", "green", "yellow"]

function nextSequence(){
    randomNumber = Math.floor(Math.random()*4)
    let randomChosenColour = buttonColour[randomNumber]
    gamePattern.push(randomChosenColour)
    $("#" + randomChosenColour).addClass("pressed")
    setTimeout(function(){
        $("#" + randomChosenColour).removeClass("pressed")
    }, 100)
}


