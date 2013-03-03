var app = app || {};

$(function() {
	'use strict';

	// Payment Item View
	// --------------

	app.UserPaymentView = Backbone.View.extend({

		// Cache the template function for a single item.
		template: _.template( $('#item-template').html() ),

		initialize: function() {
			this.listenTo(this.model, 'change', this.render);
		},

		render: function() {
			var value = this.model.get('value');
			if (value < 0)
			{
				this.model.set('value', -value);
			}
			this.$el.html( this.template( this.model.toJSON() ) );

			return this;
		}
	});
});