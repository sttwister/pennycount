var app = app || {};

(function() {
	'use strict';

	// GroupPayment Collection
	// ---------------

	// The collection of todos is backed by *localStorage* instead of a remote
	// server.
	var GroupPaymentList = Backbone.Collection.extend({

		// Reference to this collection's model.
		model: app.GroupPayment,
        url: "/api/v1/grouppayment/",

		// We keep the Payments in sequential order, despite being saved by unordered
		// GUID in the database. This generates the next order number for new items.
		nextOrder: function() {
			if ( !this.length ) {
				return 1;
			}
			return this.last().get('order') + 1;
		},

		// Payments are sorted by their original insertion order.
		comparator: function( todo ) {
			return todo.get('order');
		}
	});

	// Create our global collection of **GroupPayments**.
	app.GroupPayments = new GroupPaymentList();

}());