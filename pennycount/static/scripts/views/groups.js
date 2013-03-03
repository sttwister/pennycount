var app = app || {};

$(function() {
	'use strict';

	// Payment Item View
	// --------------

	app.GroupsView = Backbone.View.extend({

		// Cache the template function for a single item.
		template: _.template( $('#item-template').html() ),

		initialize: function() {
			this.listenTo(this.model, 'change', this.render);
		},

		render: function() {
			console.log(this.model.toJSON());

			return this;
		}
	});
});