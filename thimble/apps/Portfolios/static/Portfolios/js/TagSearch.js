var TagSearch = (function($){
	var csrftoken = "",
    checkedTags = [],
	filter = function(self, path){
		var data = {
			"csrfmiddlewaretoken":TagSearch.csrftoken,
            "tag-filters": TagSearch.checkedTags
		};

		$.ajax({
			type:"POST",
			data:data,
			url:path,
            dataType: "json",
			success:function(response){
                var resultsDiv = $('#results');
                resultsDiv.html('');
                for(var i=0; i<response.collections.length; i++){
                    resultsDiv.append('<div class="search-result">' + response.collections[i].title + '</div>');
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

			path = "/home/";

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