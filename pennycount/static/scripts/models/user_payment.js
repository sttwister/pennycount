var app = app || {};

(function() {
	'use strict';

	// UserPayment Model
	// ----------

	// Our basic **UserPayment** model.
	app.UserPayment = Backbone.Model.extend({
        urlRoot: '/api/v1/userpayment'
	});

}());
