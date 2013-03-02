var app = app || {};

(function() {
	'use strict';

	// GroupPayment Collection
	// ---------------

	var GroupPaymentList = Backbone.Collection.extend({

		// Reference to this collection's model.
		model: app.GroupPayment,
        url: "/api/v1/grouppayment/"
	});

	// Create our global collection of **GroupPayments**.
	app.GroupPayments = new GroupPaymentList();

}());
