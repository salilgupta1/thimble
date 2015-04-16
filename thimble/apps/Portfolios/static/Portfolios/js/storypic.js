$(document).ready(function() {
	//When you click on a thumbnail img in a story, make it the display img
	$(".thumb-img-wrapper > img").click(function() {
		$thumb = $(this);
		$thumbsrc = $thumb.attr('src');
		$curr = $thumb.closest('.chapter-img-wrapper').find('.cover-img > img');
		$currsrc = $curr.attr('src');
		$thumb.attr('src', $currsrc);
		$curr.attr('src', $thumbsrc);
	});
})