var ImageUpload = (function($){

	var photoUploads = 0, 
	widgetOptions = {
		cloud_name: 'thimbleapp', 
		upload_preset: 'orphans', 
		multiple:false, 
		form:'',
		cropping: 'server', 
		cropping_aspect_ratio:0.73, 
		field_name:"",
		theme:"minimal",
		thumbnails: '',
		button_caption:'',
		thumbnail_transformation: { width: 400, height: 550, crop: 'fill' }
	},
	updateNumPhotos = function(){
		photoUploads++;
		if(photoUploads > 0){
            $("#create-btn").attr("disabled",false);
        }
        if(photoUploads > 2){
            $('.supp-holder').css("display", "none");
        }
	},
	setForm = function(form){
		widgetOptions['form'] = form;
	},
	init = function(form){
		setForm(form);

		$('.cover-holder').click(function() {
			widgetOptions.field_name = 'cover_photo';
			widgetOptions.thumbnails = '.cover-group';
			cloudinary.openUploadWidget(widgetOptions,function(error, result){});
        });

		$('.supp-holder').click(function() {
			widgetOptions.field_name = 'entry_photos';
			widgetOptions.thumbnails = '.supp-group';
			cloudinary.openUploadWidget(widgetOptions,function(error, result){
				updateNumPhotos();
				// TODO error handle here
			});
		});
	};

	return {
		init:init
	};
}(jQuery));