$(document).ready(function() {

	function validate_entry(input_ids) {
		var invalid_ids = []
		var validation_error = 0;

		$.each(input_ids, function(index, value) {
			if ( !$(value).val() ) {
				$(value).addClass('validation-error');
				$('.error-list').append('<li>' + $(value).attr('data-error') + ' field required.</li>');
				validation_error = 1;
			}
			else {
				$(value).removeClass('validation-error');
			}
		});
		return validation_error;
	}

	function validate_email(email_ids) {
		var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		return regex.test($(email_ids).val());
	}

	function validate_passwords(password1, password2) {
		var password_error = 0;

		if (password1.val() !== password2.val()) {
			$(password1).addClass('validation-error');
			$(password2).addClass('validation-error');
			$('.error-list').append('<li>Password fields must match.</li>');
			password_error = 1;
		}
		if (($(password1).val()).length < 6) {
			$(password1).addClass('validation-error');
			$(password2).addClass('validation-error');
			$('.error-list').append('<li>Password must be greater than 6 characters</li>');
			password_error = 1;
		}

		return password_error;
	}

	$('#registration_submit').click(function() {
		var input_ids = [$('#username'), $('#email'), $('#password1'), $('#password2')];
		$('.error-list').empty();

		var validation_error = validate_entry(input_ids);
		var password_error = validate_passwords($('#password1'), $('#password2'));


		if (!(validate_email($('#email')))) {
			$('.message-box').show();
			$('.error-list').append('<li>Enter a valid email address</li>');
			$('#email').addClass('validation-error');
			var email_error = 1;
		}

		if (validation_error || email_error || password_error) {
			$('.message-box').show();
			return false;
		}
		

	})
});