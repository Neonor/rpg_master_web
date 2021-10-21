$(document).ready(function(){
	
	$("#carte").height($("#carte").width())
	
	$(".hexagone").each(function(){
		var hexa = $(this);
		var width = hexa.children().children().width()
		var height = hexa.children().children().height()
		var x = $("#carte").width()*3/4 -width/2 + hexa.attr("x")*width + hexa.attr("y")%2*(width/2);
		var y = $("#carte").height()/2 -height/2 + hexa.attr("y")*(-height*3/4);
		hexa.offset({ top: y, left: x })
	});
});