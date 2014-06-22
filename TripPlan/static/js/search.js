(function() {
	$("#search-form").submit(function(){
		$.get( "/search/", $( this ).serialize(), function (data) {
	    	$("#results-scrollable-div").html(data);
	    });
	    return false;
	});
})();