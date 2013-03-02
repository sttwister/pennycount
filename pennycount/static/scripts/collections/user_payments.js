var app = app || {};

(function() {
	'use strict';

	// UserPayment Collection
	// ---------------

	var UserPaymentList = Backbone.Collection.extend({

		// Reference to this collection's model.
		model: app.UserPayment,
        url: "/api/v1/userpayment/"
	});

	// Create our global collection of **Payments**.
	app.UserPayments = new UserPaymentList();

}());
