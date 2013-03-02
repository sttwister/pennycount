var app = app || {};

(function() {
	'use strict';

	// Payment Collection
	// ---------------

	var PaymentList = Backbone.Collection.extend({

		// Reference to this collection's model.
		model: app.Payment,
        url: "/api/v1/payment/"
	});

	// Create our global collection of **Payments**.
	app.Payments = new PaymentList();

}());
