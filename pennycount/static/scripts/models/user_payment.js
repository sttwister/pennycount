var app = app || {};

(function() {
	'use strict';

	// UserPayment Model
	// ----------

	// Our basic **UserPayment** model has `user`, `title`, and `value` attributes.
	app.UserPayment = Backbone.Model.extend({

        urlRoot: '/api/v1/userpayment',

		// Default attributes
		defaults: {
			title: '',
			value: 0
		},

	});

}());
