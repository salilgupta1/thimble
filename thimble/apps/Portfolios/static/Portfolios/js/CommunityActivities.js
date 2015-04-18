var CommunityActivities = (function($){
	var authenticatedUsername = "",
	csrftoken = "";

	var like = function(self, path){
		data = {
			"liker":CommunityActivities.authenticatedUsername, 
			"design_story_id":self.attr("data-storyid"),
			"csrfmiddlewaretoken":CommunityActivities.csrftoken
		};

		$.ajax({
			type:"POST",
			data:data,
			url:path,
			success:function(response){
				// update count
				count = self.siblings("p").children(".likes-count").text();
				count = parseInt(count) + 1;
				self.siblings("p").children(".likes-count").text(count);

				// change the button to unlike 
				self.children(".text").text("Unlike");
				self.removeClass("like-btn").addClass("unlike-btn");
			},
			error:function(error){
				console.log(error);
			}
		});
	}, 

	unlike = function(self, path){
		data = {
			"liker":CommunityActivities.authenticatedUsername, 
			"design_story_id":self.attr("data-storyid"),
			"csrfmiddlewaretoken":CommunityActivities.csrftoken
		};

		$.ajax({
			type:"POST",
			data:data,
			url:path,
			success:function(response){
				// update count
				count = self.siblings("p").children(".likes-count").text();
				count = parseInt(count) - 1;
				self.siblings("p").children(".likes-count").text(count);

				// change button to like
				self.children(".text").text("Like");
				self.removeClass("unlike-btn").addClass("like-btn");
			},
			error:function(error){
				console.log(error);
			}
		});
	},

	follow = function(path){
		data = {
			"follower":CommunityActivities.authenticatedUsername, 
			"followee":CommunityActivities.portfolioUsername,
			"csrfmiddlewaretoken":CommunityActivities.csrftoken
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

	unfollow = function(path){
		data = {
			"follower":CommunityActivities.authenticatedUsername, 
			"followee":CommunityActivities.portfolioUsername,
			"csrfmiddlewaretoken":CommunityActivities.csrftoken
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
		data = {
			"commenter":CommunityActivities.authenticatedUsername,
			"design_story_id": self.attr("data-storyid"),
			"csrfmiddlewaretoken":CommunityActivities.csrftoken,
			"comment":$("#id_comment").val()
		};
		$.ajax({
			type:"POST",
			data:data,
			url:path,
			success:function(response){
				// update count
				count = $("#num-comments").text();
				count = parseInt(count) + 1;
				$("#num-comments").text(count);
				e.preventDefault();
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

			path = "/"+$(this).attr("data-username")+"/like_story/";
			like($(this),path);
		}); 

		// unlike button is clicked
		$(document).on('click','.unlike-btn',function(){
			path = "/"+$(this).attr("data-username")+"/unlike_story/";
			unlike($(this), path);
		});

		// follow button is clicked
		$(document).on('click','#follow-btn',function(){
			path = "/"+$(this).attr("data-username")+"/follow/";
			follow(path);
		});

		// unfollow button is clicked
		$(document).on('click','#unfollow-btn',function(){
			path = "/"+$(this).attr("data-username")+"/unfollow/";
			unfollow(path);
		});

      	// comment is submitted
      	$(".comment-form").on("submit", function(e){
      		path="/" + $(this).attr("data-username") + "/comment/";
      		comment($(this), path, e);
      	});
	};
	return {
		// make publically accessible 
		init:init,
	};
}(jQuery));