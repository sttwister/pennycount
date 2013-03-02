var app = app || {};

(function() {
	'use strict';

	// Payment Model
	// ----------

	// Our basic **Payment** model has `user`, `title`, and `value` attributes.
	app.Payment = Backbone.Model.extend({

        urlRoot: '/api/v1/payment',

		// Default attributes
		defaults: {
			title: '',
			value: 0
		},

	});

}());
