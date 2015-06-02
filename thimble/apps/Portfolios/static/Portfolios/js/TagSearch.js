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
                var resultsDiv = $('#results');
                resultsDiv.html('');
                console.log(response.collections);
                for(var i=0; i<response.collections.length; i++){
                	var url = response.add_info[response.collections[i].title]
                    resultsDiv.append('<div><a href="'+ url +'">' + response.collections[i].title + '</a></div>');
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