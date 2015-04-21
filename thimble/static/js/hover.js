var hideoverlay = true;

$(document).ready(function() 
{


	if ($(this).width() > 767) {
		hideoverlay = false;
	}
	else if ($(this).width() <= 767) {
		hideoverlay = true;
	}

	$('.piece-thumb-container').hover(function() {
		if (hideoverlay == false) {
			$overlay = $(this).children(":first");
			$overlay.fadeTo("fast", 1);
		}
	}, function() {
		if (hideoverlay == false) {
			$overlay = $(this).children(":first");
			$overlay.fadeTo("fast", 0);
		}
	});

});