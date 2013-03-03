var app = app || {};

(function() {
	'use strict';

	// Group Collection
	// ---------------

	var GroupList = Backbone.Collection.extend({

		// Reference to this collection's model.
		model: app.Group,
        url: "/api/v1/group/"
	});

	// Create our global collection of **Groups**.
	app.Groups = new GroupList();

}());
