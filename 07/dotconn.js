// Jionghao Wu, Joseph Yusufov
// SoftDev Pd. 2
// K #06: Dot Dot Dot
// 2020-02-12

//retrieve node in DOM via ID
var c = document.getElementById("slate")

//instantiate a Canvas Rendering 2D object
var ctx = c.getContext("2d")

//invoke interface methods
ctx.fillStyle="#ff0000" //red
//ctx.fillRect(50,50,100,200)
var can = c.getBoundingClientRect();
var shape = "rect";
var lastX = 0;
var lastY = 0;

var clear = function(){
    var width = c.width;
    var height = c.height;
    ctx.clearRect(0,0,width,height);
    lastX = 0;
    lastY = 0;
}
var start = null;
var animate = function startAnim(timestamp){
	if(!start) start = timestamp;
	var progress = timestamp - start
	console.log(start)
	var x = 300;
        var y = 300;
	ctx.beginPath();
	ctx.arc(x,y,progress/10, 0, 2 * Math.PI);
	ctx.fill();
	window.requestAnimationFrame(startAnim);
}


var animation = document.getElementById("animate");
animation.addEventListener("click",animate);
var clearing = document.getElementById("clear");
clearing.addEventListener("click",clear);
