$(function() {

	$('#loginbutton').click(function() {
		$.loadmodal({
					url: '/account/login/',
					id: 'loginmodal',
					title: 'Login',
					width: '400px',
			
		});
			

		
	});//click
	
	
	
}); //ready

$(function() {

	$('#editbutton').click(function() {
		$.loadmodal({
					url: '/manager/areasedit/',
					id: 'editmodal',
					title: 'Edit Area',
					width: '400px',
			
		});
			

		
	});//click
	
	
	
}); //ready

  /*  $.loadmodal({
      url: '/your/server/url',
      id: 'my-modal-id',
      title: 'My Title',
      width: '400px',
      closeButton: false,
      buttons: {
        "OK": function() {
          // do something here
          // a false return here cancels the automatic closing of the dialog
        },  
        "Cancel": false,   // no-op - just having the option makes the dialog close
      },
      modal: {
        keyboard: false,
        // any other options from the regular $().modal call (see Bootstrap docs)
      },
      ajax: {
        dataType: 'html',
        method: 'GET',
        success: function(data, status, xhr) {
          console.log($('#custom_modal_id'));
        },//
        // any other options from the regular $.ajax call (see JQuery docs)
      },
      onShow: function(dlg) {
        console.log('The dialog just showed on the screen!');
        console.log(dlg);
      },
    });

Closing a dialog: (this is standard bootstrap)
    
    $('#my-modal-id').modal('hide'); 


*/
		
		$('#id_ptype').change(function() {
				console.log("Change");
			
			var v = $(this).val();
			console.log(v);
			
			$("#id_creator").closest("p").toggle(v=="IndividualProduct");
			$("#id_date_made").closest("p").toggle(v=="IndividualProduct");
			$("#id_status").closest("p").toggle(v=="RentalProduct");
			$("#id_quantity").closest("p").toggle(v=="BulkProduct");
			
			
		});
		
		$('#id_ptype').change();
