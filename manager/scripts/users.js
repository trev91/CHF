
$(function() {

	$('.delete_button').click(function(e){
		e.preventDefault();
		var theHREF = $(this).attr('href');
		// the Uid's href will match the theHREF's href.
		$('#confirm_delete_button').attr('href', theHREF);
		$('#delete_modal').modal('show');
		
	});
});


 