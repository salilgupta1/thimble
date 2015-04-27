var openmenu = false;

$(document).ready(function() 
{


	if ($(this).width() > 767) {
		hideoverlay = false;
	}
	else if ($(this).width() <= 767) {
		hideoverlay = true;
	}

	$('.navbar-toggle').click(function() {
		$('.navbar-nav > .dropdown').toggleClass('open');
	});

});