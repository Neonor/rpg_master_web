$(document).ready(function(){
	$.ajaxSetup({ cache: false });

	$( "#dialog" ).hide();
	$( "#close_dialog" ).click(function(){
		$( "#dialog" ).hide()
	})

	dialog = function(link,name){
		$.get(link,function(data){
			$( "#dialog .card-body" ).html(data);
			$( "#dialog_title").text(name)

			$("#dialog form").each(function(){
				$(this).submit(function(e) {
				
				    e.preventDefault(); // avoid to execute the actual submit of the form.
				
				    var form = $(this);
				    
				    $.ajax({
				           type: "POST",
				           url: link,
				           data: form.serialize(), // serializes the form's elements.
				           success: function()
				           {
								$( "#dialog" ).hide();
								location.reload();
				           }
				         });
				});
			})
			$( "#dialog" ).show();
		});
	}
	
	
	$(".dialog").each(function(){
		$(this).click(function(){
			dialog($(this).attr("link"),$(this).attr("name"))
		});
	})
	
});