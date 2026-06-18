console.log("JS funcionando!!")

let gamePattern = []
let userClickedPattern = []
let randomNumber

const buttonColor = ["red", "blue", "green", "yellow"]

function nextSequence(){
    randomNumber = Math.floor(Math.random()*4)
    let randomChosenColor = buttonColor[randomNumber]
    gamePattern.push(randomChosenColor)

    let audio = new Audio("sounds/" + randomChosenColor + ".mp3")
    audio.play()

    $("#" + randomChosenColor).addClass("pressed")
    setTimeout(function(){
        $("#" + randomChosenColor).removeClass("pressed")
    }, 100)
}

$(".btn").click(function() {
    let userChosenColor = $(this).attr("id")
    userClickedPattern.push(userChosenColor)
    console.log(userClickedPattern)
})


