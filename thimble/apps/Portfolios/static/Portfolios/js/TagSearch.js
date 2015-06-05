var TagSearch = (function($){
	var csrftoken = "",
    checkedTags = [],
    username = "",
	filter = function(self, path){
		var data = {
			"csrfmiddlewaretoken":TagSearch.csrftoken,
            "tag-filters": TagSearch.checkedTags,
            "username": TagSearch.username
		};

		$.ajax({
			type:"POST",
			data:data,
			url:path,
            dataType: "json",
			success:function(response){
                var url, template,
                resultsDiv = $('#results');
               	template = $('.collection-container:first');
                resultsDiv.html('');
                for(var i=0; i<response.collections.length; i++){
                	
                	url = response.collections[i].url
                	var title = response.collections[i].title;

                	template.find('.collection-title').text(title);
                	template.find('.collection-description').text(response.collections[i].description);
                	template.find('.collection-url').attr('href',url);
                	
                	template.find('.thumb-container').html('');

                	var photos = response.collections[i].pieces;
                	var num_photos = photos.length > 4 ? 4: photos.length;
                	for (var p = 0; p < num_photos; p++){
                		var cloudinary = $.cloudinary.image(photos[p], {class:'img-responsive thumb-img'});
                		template.find('.thumb-container').append(cloudinary);
                	}

                	resultsDiv.append(template);
                	template = template.clone();
                }
			},
			error:function(error){
				console.log(error);
			}
		});
	},

	init = function(){
		var path;

		// tag is checked
		$(document).on('click','.tag-filter',function(){
			path = "/dashboard/" + TagSearch.username;

            // get all checked tags
            TagSearch.checkedTags = $('.tag-filter:checkbox:checked').map(function() {
                return this.value;
            }).get();

			filter($(this), path);
		});

	};
	return {
		// make publically accessible 
		init:init
	};
}(jQuery));