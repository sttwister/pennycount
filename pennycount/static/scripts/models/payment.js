var app = app || {};

(function() {
	'use strict';

	// Payment Model
	// ----------

	// Our basic **Payment** model.
	app.Payment = Backbone.Model.extend({
        urlRoot: '/api/v1/payment'
	});

}());
