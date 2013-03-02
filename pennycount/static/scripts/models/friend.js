var app = app || {};

(function() {
	'use strict';

	// Friend Model
	// ----------

	// Our basic **Friend** model.
	app.Friend = Backbone.Model.extend({
		urlRoot: '/api/v1/friend'
	});

}());
