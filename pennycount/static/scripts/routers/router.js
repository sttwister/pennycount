var app = app || {};

(function() {
	'use strict';

	// Todo Router
	// ----------

	var Workspace = Backbone.Router.extend({
		routes:{
			'*actions': 'defaultRoute'
		}
	});

	app.Router = new Workspace();
    app.Router.on('route:defaultRoute', function(actions) {

    });

	Backbone.history.start();
}());
