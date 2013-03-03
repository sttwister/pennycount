var app = app || {};

(function() {
	'use strict';

	// Group Model
	// ----------

	// Our basic **Group** model.
	app.Group = Backbone.Model.extend({
		urlRoot: '/api/v1/group'
	});

}());
