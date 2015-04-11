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
				self.children(".text").text("Unlike");
				self.removeClass("like-btn").addClass("unlike-btn");
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
				$("#follow-btn").text("Follow");
			},
			error:function(error){
				console.log(error);
			}
		});
	},

	comment = function(path){

	};

	return {
		// make publically accessible 
		like:like,
		follow:follow,
	};
}(jQuery));