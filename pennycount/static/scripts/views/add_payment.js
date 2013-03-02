var app = app || {};

$(function() {
	'use strict';

	// Payment Item View
	// --------------

	app.AddPaymentView = Backbone.View.extend({

		el: '#add-payment-div',

		events: {
			'click .add-payment':	'addPayment',
		},

		initialize: function() {
		//	this.render();
		},

		render: function() {
			return this;
		},

		addPayment: function() {
			var payment = new app.GroupPayment();

			payment.save();	
		}
	});
});