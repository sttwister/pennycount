var app = app || {};

(function() {
	'use strict';

	// Friend Model
	// ----------

	// Our basic **Friend** model has `name` attribute.
	app.Friend = Backbone.Model.extend({

		// Default attributes
		defaults: {
			name: ''
		}
	});

}());
