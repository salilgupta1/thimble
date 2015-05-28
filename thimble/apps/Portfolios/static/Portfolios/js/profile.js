$(document).ready(function() {
	$(".thumb-container").each(function() {
		var mywidth = $(this).children().first().width();
		var container_width = (mywidth + 10) * $(this).children().length;
		container_width += $(".det-container").width();
		$(this).css("width", container_width);
	});
	
});