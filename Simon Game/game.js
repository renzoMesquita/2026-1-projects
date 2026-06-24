let gamePattern = []
let userClickedPattern = []
let randomNumber

let level = 0;

const buttonColor = ["red", "blue", "green", "yellow"]

function nextSequence(){
    randomNumber = Math.floor(Math.random()*4)
    let randomChosenColor = buttonColor[randomNumber]
    gamePattern.push(randomChosenColor)

    let audio = new Audio("sounds/" + randomChosenColor + ".mp3")
    audio.play()

    level++

    $("h1").html("Level " + level)

    $("#" + randomChosenColor).addClass("pressed")
    setTimeout(function(){
        $("#" + randomChosenColor).removeClass("pressed")
    }, 100)
}

let started = false

$(document).keypress(function(){
    $("h1").html("Level " + level)
    $("h1").addClass("level-title")
    if(!started){
        nextSequence()
        started = true
    }
})

$(".btn").click(function() {
    let userChosenColor = $(this).attr("id")
    userClickedPattern.push(userChosenColor)

    $("#" + userChosenColor).addClass("pressed")
    setTimeout(function(){
        $("#" + userChosenColor).removeClass("pressed")
    }, 100)

    let audio = new Audio("sounds/" + userChosenColor + ".mp3")
    audio.play()

    console.log(userClickedPattern)
})


