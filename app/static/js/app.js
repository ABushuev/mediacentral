( function() {
	var app=angular.module('gemStore',[]);
	var name='Alexei';
	app.controller('User',function(){
		this.name=name
	})
})();