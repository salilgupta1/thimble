var CommunityActivities = (function($){
	var portfolioUsername = "",
	authenticatedUsername = "",
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

	comment = function(path){

	},
	init = function(){
		var path;

		// like button is clicked
		$(".like-btn").on("click", function(){
			path = "/"+CommunityActivities.portfolioUsername+"/like_story/";
			like($(this),path);
		}); 

		// unlike button is clicked
		$(".unlike-btn").on("click", function(){
			path = "/"+CommunityActivities.portfolioUsername+"/unlike_story/";
			unlike($(this), path);
		});

		// follow button is clicked
		$("#follow-btn").on("click", function() {
			path = "/"+CommunityActivities.portfolioUsername+"/follow/";
			follow(path);
		});

		// unfollow button is clicked
		$("#unfollow-btn").on("click", function(){
			path = "/"+CommunityActivities.portfolioUsername+"/unfollow/";
			unfollow(path);
		});

      	// comment is submitted
	};
	return {
		// make publically accessible 
		init:init,
	};
}(jQuery));