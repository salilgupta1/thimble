var ImageUpload = (function($){

	var init = function(cloudName){
		$('#photos_upload_widget').cloudinary_upload_widget(
			{
				cloud_name: cloudName, 
				upload_preset: 'orphans', 
				cropping: 'server', 
				cropping_aspect_ratio:0.73, 
				button_caption:"Add Images", 
				field_name:"images",
				theme:"minimal",
				thumbnails:"#images",
				thumbnail_transformation: 
				{ 
					width: 200,
					height: 275,
					crop: 'fill' 
				}
			},
			function(error, result) {}
		);

		$("#avatar_upload_widget").cloudinary_upload_widget(
			{
                cloud_name:cloudName, 
                upload_preset:"orphans", 
                multiple: false,
                cropping: 'server', 
                cropping_aspect_ratio:1.0, 
                button_caption:"Change Avatar", 
                field_name:"avatar",
                theme:"minimal",
                thumbnail_transformation:
                {
                    width: 100, 
                    height: 133,
                    crop: 'limit' 
                }
            },function(error, result){}
		);
	};

	return {
		init:init
	};
}(jQuery));