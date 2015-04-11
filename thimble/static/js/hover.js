$(document).ready(function() 
{

	$('.piece-thumb-container').hover(function() {
		$overlay = $(this).children(":first");
		$overlay.fadeTo("fast", 1);
	}, function() {
		$overlay = $(this).children(":first");
		$overlay.fadeTo("fast", 0);
	});

});