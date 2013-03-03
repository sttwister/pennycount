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
		},

		render: function() {
			return this;
		},

		addPayment: function() {
			console.log("DSADSA");
			var payment = new app.GroupPayment();

			var friends = $("#friends-input").val();
			friends = _.map(friends, function ( friend_id ) {
				return { pk: friend_id };
			});

			payment.set({title: $("#title").val(), 
				value: $("#value").val(),
				shared_with: friends
			});

            payment.save();
            location.reload();

            $("#title").val("");
            $("#value").val("");
            $("#friends-input").val("").trigger("liszt:updated");
		}
	});
});
