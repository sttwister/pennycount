var app = app || {};

$(function() {
	'use strict';

	// Payment Item View
	// --------------

	// The DOM element for a todo item...
	app.UserPaymentView = Backbone.View.extend({

		//... is a list tag.
		tagName:  'li',

		// Cache the template function for a single item.
		template: _.template( $('#item-template').html() ),

		initialize: function() {
			this.listenTo(this.model, 'change', this.render);
		},

		render: function() {
			this.$el.html( this.template( this.model.toJSON() ) );

			return this;
		}
	});
});