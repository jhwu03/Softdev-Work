// Jionghao Wu
// SoftDev pd2
// K08: What is it saving the screen from
// 2020-02-14



//instantiate a Canvas Rendering 2D object
var c = document.getElementById("slate")
var ctx = c.getContext("2d")
var radius = 0;
var stop = true;
var id = null;
var increase = true;
var state = null;
//invoke interface methods
ctx.fillStyle="#ff0000" //red
//ctx.fillRect(50,50,100,200)

var animate = function(event){
  ctx.clearRect(0,0,c.width,c.height);
  ctx.beginPath();
  ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI);
  ctx.fill();
  if (radius == 0){
    increase = true;
  }
  if (radius == c.width / 2 || radius == c.length / 2){
    increase = false;
  }
  if (increase){
    radius++;
  }
  else{
    radius--;
  }
  id1 = requestAnimationFrame(animate);
  stop = false;
  state = 1;
};



var xcor = 100;
var ycor = 100;
var dirList = ['SE','SW','NE','NW']
var direction = 'NE';
var dvdjpg = document.getElementById("dvd-image");

var randomDvd = function() {
    xcor = Math.floor(Math.random() * 400);
    ycor = Math.floor(Math.random() * 400);
    direction = dirList[Math.floor(Math.random() * 4)];
}

var go = function(){
  randomDvd();
  DVDanim();
}

var DVDanim = function(event){
  id2 = window.requestAnimationFrame(DVDanim);
  ctx.clearRect(0,0,c.width,c.height);
  ctx.drawImage(dvdjpg,xcor,ycor,100,70);
  if(xcor == 500) {
    if(direction == "NE"){
      direction = "NW";}
    if(direction == "SE"){
      direction = "SW";}
  }
  if(xcor == 0) {
    if(direction == "NW"){
      direction = "NE";}
    if(direction == "SW"){
      direction = "SE";}
  }
  if(ycor == 530) {
    if(direction == "SE"){
      direction = "NE";}
    if(direction == "SW"){
      direction = "NW";}
  }
  if(ycor == 0) {
    if(direction == "NE"){
      direction = "SE";}
    if(direction == "NW"){
      direction = "SW";}
  }

  if(direction == "NE"){
    xcor += 1;
    ycor -= 1;
  }
  if(direction == "SE"){
    xcor += 1;
    ycor += 1;
  }
  if(direction == "NW"){
    xcor -= 1;
    ycor -= 1;
  }
  if(direction == "SW"){
    xcor -= 1;
    ycor += 1;
  }
  stop = false;
  state = 2;
}

var halt = function(event){
  if (stop){
    event.preventDefault();
  }
  else{
    if (state == 1){
    window.cancelAnimationFrame(id1);
    }
    if(state == 2){
    window.cancelAnimationFrame(id2);
    }
    stop = true;
  }
}








var button1 = document.getElementById('animate');
button1.addEventListener('click', function(event){
  if (!stop){
    event.preventDefault();
  }
  else{
    animate();
  }
});

var button2 = document.getElementById('stop');
button2.addEventListener('click', halt);

var button3 = document.getElementById('DVD');
button3.addEventListener('click', function(event){
  if (!stop){
    event.preventDefault();
  }
  else{
    go();
  }
});
