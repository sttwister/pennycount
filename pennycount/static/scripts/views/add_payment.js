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

			var friends = $("#friends-input").tokenInput("get");
			friends = _.map(friends, function ( friend ) {
				return {pk:friend.id};
			});

			payment.set({title: $("#title").val(), 
				value: $("#value").val(),
				share_with: friends
			});

			console.log($("#friends-input").tokenInput("get"));

			payment.save();	
		}
	});
});