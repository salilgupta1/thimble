var voted = 0;

$(document).ready(function() 
{
	$('.vote-yes').click(function() {
		var parent = $(this).parent()
		parent.css('background-color', '#26a65b');
		parent.children('img').fadeTo('slow', 0.7);
		voted++;
		showDone();
	});

	$('.vote-no').click(function() {
		var parent = $(this).parent()
		parent.css('background-color', '#ef4836');
		parent.children('img').fadeTo('slow', 0.7);
		voted++;
		showDone();
	});

	function showDone() {
		if(voted > 2) {
			$('.footer').css('display', 'inline');
		}
	}

	$('.info').click(function() {
		var currImg = $(this).parent().children('img');
		$("#modal-img").attr("src", currImg.attr('src'));
		$('.modal').modal('show');
	});

	$('.shop-container').click(function() {
		var currImg = $(this).children('img');
		$("#modal-img").attr("src", currImg.attr('src'));
		$('.modal').modal('show');
	});
});