$("#search-form").submit(function(){
	$.ajax( '/search/' + document.getElementById('yelpSearch-location').value + '/' + document.getElementById('yelpSearch-keyword').value +'/' )
	.done(function(data) {
    	$("#results-scrollable-div").html(data);
    });
    return false;
});