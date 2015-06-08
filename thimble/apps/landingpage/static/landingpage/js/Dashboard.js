var Dashboard = (function($){
	var csrftoken = "",
    checkedTags = [],
    username = "",
    userImage="",
	filter = function(self, path){
		var data = {
			"csrfmiddlewaretoken":Dashboard.csrftoken,
            "tag-filters": Dashboard.checkedTags,
            "username": Dashboard.username
		};

		$.ajax({
			type:"POST",
			data:data,
			url:path,
            dataType: "json",
			success:function(response){
                renderCollection(response.collections);
			},
			error:function(error){
				console.log(error);
			}
		});
	},
    filterBuyers = function(self, path){
        var data = {
            "csrfmiddlewaretoken":Dashboard.csrftoken,
            "tag-filters": Dashboard.checkedTags,
        };
        $.ajax({
            type:"POST",
            data:data,
            url:path,
            dataType: "json",
            success:function(response){
                var template = $(".followee:first"), 
                cloudinary;
                $(".following-list").html("");

                for (var i = 0; i < response.buyers.length; i++){
                    template.find('.followee-name').text(response.buyers[i].user__first_name +" "+response.buyers[i].user__last_name);
                    template.find('.followee-location').text(response.buyers[i].location);
                    template.find('.followee-bio').text(response.buyers[i].bio);
                    template.find('.followee-boutique').text(response.buyers[i].boutique_name);

                    if (response.buyers[i].avatar == ""){
                        cloudinary = "<img src='"+Dashboard.userImage+"' class='img-profile img-responsive img-circle'/>";
                    }
                    else{
                        cloudinary = $.cloudinary.image(response.buyers[i].avatar, {class:'img-responsive img-circle img-profile'});
                    }
                    template.find('.followee-avatar').html(cloudinary);

                    $(".following-list").append(template);
                    template = template.clone();
                }
            },
            error:function(error){
                console.log(error);
            }
        });

    },
    favoriteList = function(self, path){
        var data = {
            "csrfmiddlewaretoken":Dashboard.csrftoken
        };
        $.ajax({
            type:"POST",
            data:data,
            url: path,
            dataType:"json",
            success:function(response){
                renderCollection(response.collections);
            },
            error:function(response){
                console.log(response);
            }
        });

    },
    followList = function(self, path){
        var data = {
            "csrfmiddlewaretoken":Dashboard.csrftoken
        };
        $.ajax({
            type:"POST",
            data:data,
            url: path,
            dataType:"json",
            success:function(response){
                $('#results').hide();
                $(".following-list").show();
                var template = $(".followee:first");
                $(".following-list").html("");

                for (var i = 0; i < response.following.length; i++){
                    template.find('.followee-name').text(response.following[i].user__first_name +" "+response.following[i].user__last_name);
                    template.find('.followee-location').text(response.following[i].location);
                    template.find('.followee-bio').text(response.following[i].bio);

                    if (response.following[i].avatar == ""){
                        cloudinary = "<img src='"+Dashboard.userImage+"' class='img-profile img-responsive img-circle'/>";
                    }
                    else{
                        cloudinary = $.cloudinary.image(response.following[i].avatar, {class:'img-responsive img-circle img-profile'});
                    }
                    template.find('.followee-avatar').html(cloudinary);
                    template.attr('href',"/"+response.following[i].user_id + "/");
                    $(".following-list").append(template);
                    template = template.clone();
                }

            },
            error:function(response){
                console.log(response);
            }
        });
    },
    renderCollection = function(collections){
        $(".following-list").hide();
        $("#results").show();   

        var template,
        resultsDiv = $('#results');
        template = $('.collection-container:first');
        resultsDiv.html("");

        for(var i=0; i<collections.length; i++){
            
            var url = collections[i].url;
            template.find('.designer-name').text(collections[i].designer__user__first_name +" "+ collections[i].designer__user__last_name);
        
            if (collections[i].avatar == ""){
                cloudinary = "<img src='"+Dashboard.userImage+"' class='img-profile img-responsive img-circle'/>";
            }
            else{
                cloudinary = $.cloudinary.image(collections[i].designer__avatar, {class:'img-responsive img-circle img-profile'});
            }
            template.find('.designer-avatar').html(cloudinary);
            template.find('.collection-title').text(collections[i].title);

            template.find('.collection-description').text(collections[i].description);
            template.find('.collection-url').attr('href',url);
            
            template.find('.thumb-container').html('');

            var photos = collections[i].pieces;
            var num_photos = 4;

            if (num_photos > photos.length){
                num_photos = photos.length;
            }

            for (var p = 0; p < num_photos; p++){
                var cloudinary = $.cloudinary.image(photos[p], {class:'img-responsive thumb-img'});
                template.find('.thumb-container').append(cloudinary);
            }

            resultsDiv.append(template);
            template = template.clone();
        }
    },
	init = function(){
		var path;

		// tag is checked
		$(document).on('click','.tag-filter',function(){
			path = "/filter-collections/";

            // get all checked tags
            Dashboard.checkedTags = $('.tag-filter:checkbox:checked').map(function() {
                return this.value;
            }).get();

			filter($(this), path);
		});
        $(document).on('click','.buyer-filter',function(){
            path = "/"+Dashboard.username+"/filter-buyers/";

            // get all checked tags
            Dashboard.checkedTags = $('.buyer-filter:checkbox:checked').map(function() {
                return this.value;
            }).get();

            filterBuyers($(this), path);
        });


        $(document).on('click', '.following-header', function(){
            path = "/list-followers/";
            followList($(this), path);
        });

        $(document).on('click', '.favorites', function(){
            path = "/list-favorites/";
            favoriteList($(this), path);
        });

	};
	return {
		// make publically accessible 
		init:init
	};
}(jQuery));