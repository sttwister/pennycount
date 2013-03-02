var app = app || {};

(function() {
	'use strict';

	// Friend Collection
	// ---------------

	var FriendList = Backbone.Collection.extend({

		// Reference to this collection's model.
		model: app.Friend,
        url: "/api/v1/friend/"
	});

	// Create our global collection of **Friends**.
	app.Friends = new FriendList();

}());
