var numSquares = 6;
var colors = [];
var pickedColor;
var squares = document.querySelectorAll(".square");
var colorDisplay = document.getElementById("colorDisplay")
var messageDisplay = document.querySelector("#message");
var h1 = document.querySelector("h1");
var resetButton = document.querySelector("#reset");
var modeButtons = document.querySelectorAll(".mode");

init ();

function init(){
    // New Mode btn event listeners: 
    for(var i = 0; i < modeButtons.length; i++) {
        modeButtons[i].addEventListener("click", function(){
            //remove 'selected' class from both btn, add to clicked btn
            modeButtons[0].classList.remove("selected");
            modeButtons[1].classList.remove("selected");
            this.classList.add("selected");
            //figure out how many squares to show
            this.textContent === "Easy" ? numSquares = 3: numSquares = 6;
            //pick new colors
            //pick a new pickedColor
            //update page to reflect changes
            reset ();
        })
    };
    //Click listeners for squares, logic for comparing colors
    for(var i  = 0; i < squares.length; i++) {
        //Add click listeners to squares
        squares[i].addEventListener("click", function (){
            //Grab color of clicked square
            var clickedColor = this.style.backgroundColor;
            //Compare clicked color to pickedColor
            if (clickedColor === pickedColor) {
                messageDisplay.textContent = "Correct";
                changeColor(clickedColor);
                h1.style.backgroundColor = clickedColor;
                resetButton.textContent = "Play Again?";
            } else {
                this.style.backgroundColor = "#232323";
                messageDisplay.textContent = "Try Again!";
            }
        });
    };
    //Generate new colors, reset text on page
    reset();
}

function changeColor(color) {
    //Loop through all squares
    for(var i = 0; i < squares.length; i++){
    //Change color to match correct color
        squares[i].style.background = color;
    }
}

function pickColor() {
    var random = Math.floor(Math.random() * colors.length);
    return colors[random];
}

function generateRandomColors(num){
    //make an array
    var arr = [];
    //repeat num times
    for(var i = 0; i < num; i++){
        //get random color and push into array
        arr.push(randomColor())
    }
    //return array
    return arr; 
}

function randomColor(){
    //pick a "red" from 0-255
    var r = Math.floor(Math.random() * 256) 
    //pick a "green" from 0-255
    var g = Math.floor(Math.random() * 256) 
    //pick a "blue" from 0-255
    var b = Math.floor(Math.random() * 256) 
    return "rgb(" + r + ", " + g + ", " + b + ")";
}

resetButton.addEventListener("click", function(){
    reset();
});

// Old Mode button code:

// easyBtn.addEventListener("click", function(){
//     hardBtn.classList.remove("selected");
//     easyBtn.classList.add("selected");
//     numSquares = 3;
//     colors = generateRandomColors(numSquares);
//     pickedColor = pickColor();
//     colorDisplay.textContent = pickedColor;
//     for(var i = 0; i < squares.length; i++) {
//         if(colors[i]){
//             squares[i].style.background = colors[i];
//         } else {
//             squares[i].style.display = "none";
//         }
//     }
// })

// hardBtn.addEventListener("click", function(){
//     easyBtn.classList.remove("selected");
//     hardBtn.classList.add("selected");
//     numSquares = 6
//     colors = generateRandomColors(numSquares);
//     pickedColor = pickColor();
//     colorDisplay.textContent = pickedColor;
//     for(var i = 0; i < squares.length; i++) {
//             squares[i].style.background = colors[i];
//             squares[i].style.display = "block";
//     }
// })



function reset() {
    //generate new color array
    colors = generateRandomColors(numSquares);
    //pick a new color from the array
    pickedColor = pickColor();
    //change colorDisplay to match picked color
    colorDisplay.textContent = pickedColor;
    resetButton.textContent = "New Colors";
    messageDisplay.textContent = "";
    //change colors of squares to new array colors
    for(var i = 0; i < squares.length; i++) {
        if(colors[i]){
            squares[i].style.display = "block";
            squares[i].style.background = colors[i];
        } else {
            squares[i].style.display = "none";
        }
    }
    //change button text
    resetButton.textContent = "New Colors";
    //change h1 color
    h1.style.backgroundColor = "steelblue";
    //remove winning message
}