// Jionghao Wu, Joseph Yusufov
// SoftDev Pd. 2
// K #07: They lock us in the tower whenever we get caught
// 2020-02-12

//retrieve node in DOM via ID


//instantiate a Canvas Rendering 2D object
var c = document.getElementById("slate")
var ctx = c.getContext("2d")
var radius = 0;
var stop = true;
var id = null;
var increase = true;
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
  id = requestAnimationFrame(animate);
  stop = false;
};

var halt = function(event){
  if (stop){
    event.preventDefault();
  }
  else{
    cancelAnimationFrame(id);
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
