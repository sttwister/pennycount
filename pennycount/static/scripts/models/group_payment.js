var app = app || {};

(function() {
	'use strict';

	// GroupPayment Model
	// ----------

	// Our basic **GroupPayment** model.
	app.GroupPayment = Backbone.Model.extend({
        urlRoot: '/api/v1/grouppayment'
	});

}());
