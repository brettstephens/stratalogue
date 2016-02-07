$(document).ready(function() {

	function validate_entry(input_ids) {
		var invalid_ids = []
		var validation_error = 0;

		$.each(input_ids, function(index, value) {
			if ( !$(value).val() ) {
				invalid_ids += value;
				validation_error = 1;
			}
			else if (validate_email)
		});
		return [invalid_ids, validation_error];
	}

	function validate_email(email_ids) {
		var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		return regex.test($(email_id).val());
	}

	$('#registration_submit').click(function() {
		var input_ids = [$('#username'), $('#email'), $('#password1'), $('#password2')];
		var validate_results = validate_entry(input_ids);

		if (validate_results[1]) {
			var invalid_ids = validate_results[0];

		}
		


	})
});