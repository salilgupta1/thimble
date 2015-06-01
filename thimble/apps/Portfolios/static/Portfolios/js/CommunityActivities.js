var CommunityActivities = (function($){
	var csrftoken = "",
	like = function(self, path){
		var data = {
			"collection_id":self.attr("data-collectionid"),
			"csrfmiddlewaretoken":CommunityActivities.csrftoken,
			"is_liking":1
		};

		$.ajax({
			type:"POST",
			data:data,
			url:path,
			success:function(response){
				// update count
				count = self.children(".likes-count").text();
				count = parseInt(count) + 1;
				self.children(".likes-count").text(count);

				// change the button to unlike 
				self.children(".text").text("Favorited");
				self.removeClass("like-btn").addClass("unlike-btn");
			},
			error:function(error){
				console.log(error);
			}
		});
	}, 

	unlike = function(self, path){
		var data = {
			"collection_id":self.attr("data-collectionid"),
			"csrfmiddlewaretoken":CommunityActivities.csrftoken,
			"is_liking":0
		};

		$.ajax({
			type:"POST",
			data:data,
			url:path,
			success:function(response){
				// update count
				count = self.children(".likes-count").text();
				count = parseInt(count) - 1;
				self.children(".likes-count").text(count);

				// change button to like
				self.children(".text").text("Favorite");
				self.removeClass("unlike-btn").addClass("like-btn");
			},
			error:function(error){
				console.log(error);
			}
		});
	},

	follow = function(self, path){
		var data = {
			"csrfmiddlewaretoken":CommunityActivities.csrftoken,
			"is_following":1
		};

		$.ajax({
			type:"POST",
			data:data,
			url:path,
			success:function(response){
				// update count
				count = $(".text-followers").children("span").text();
				count = parseInt(count) + 1;
				$(".text-followers").children("span").text(count);

				// change button 
				$("#follow-btn").text("Following");
				$("#follow-btn").attr("id","unfollow-btn");
			},
			error:function(error){
				console.log(error);
			}
		});
	},

	unfollow = function(self, path){
		var data = {
			"csrfmiddlewaretoken":CommunityActivities.csrftoken,
			"is_following":0
		};

		$.ajax({
			type:"POST",
			data:data,
			url:path,
			success:function(response){
				// update count
				count = $(".text-followers").children("span").text();
				count = parseInt(count) - 1;
				$(".text-followers").children("span").text(count);

				// change button text
				$("#unfollow-btn").text("Follow");
				$("#unfollow-btn").attr("id","follow-btn");

			},
			error:function(error){
				console.log(error);
			}
		});
	},

	comment = function(self, path, e){
		var data = {
			"collection_id": self.attr("data-collectionid"),
			"csrfmiddlewaretoken": CommunityActivities.csrftoken,
			"comment": $("#id_comment").val()
		};
		$.ajax({
			type:"POST",
			data:data,
			url:path,
			success:function(response){
				// update comment count
				count = $("#num-comments").text();
				count = parseInt(count) + 1;
				$("#num-comments").text(count);
				$("#id_comment").val("");
				
				// add comment
				commentDiv = '<div class="commenter-wrapper">\
								<p class="commenter-name">'+self.attr("data-commenter")+'</p>\
								<p class="comment">'+data['comment']+'</p>\
							  </div>';
				$(".comment-bin").append(commentDiv);
			},
			error:function(error){
				console.log(error);
			}
		});	
	},

	init = function(){
		var path;

		// like button is clicked
		$(document).on('click','.like-btn',function(){

			path = "/"+$(this).attr("data-username")+"/liking/";
			like($(this), path);
		}); 

		// unlike button is clicked
		$(document).on('click','.unlike-btn',function(){
			path = "/"+$(this).attr("data-username")+"/liking/";
			unlike($(this), path);
		});

		// follow button is clicked
		$(document).on('click','#follow-btn',function(){
			path = "/"+$(this).attr("data-username")+"/following/";
			follow($(this), path);
		});

		// unfollow button is clicked
		$(document).on('click','#unfollow-btn',function(){
			path = "/"+$(this).attr("data-username")+"/following/";
			unfollow($(this), path);
		});

      	// comment is submitted
      	$(".comment-form").on("submit", function(e){
      		path="/" + $(this).attr("data-username") + "/comment/";
      		comment($(this), path);
      		e.preventDefault();
      	});
	};
	return {
		// make publically accessible 
		init:init,
	};
}(jQuery));