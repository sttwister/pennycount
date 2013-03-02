var app = app || {};

(function() {
	'use strict';

	// GroupPayment Model
	// ----------

	// Our basic **GroupPayment** model has `user`, `title`, and `value` attributes.
	app.GroupPayment = Backbone.Model.extend({
        urlRoot: '/api/v1/grouppayment',

		// Default attributes
		defaults: {
			title: '',
			value: 0
		},

	});

}());
