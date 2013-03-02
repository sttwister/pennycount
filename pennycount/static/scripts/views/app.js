var app = app || {};

$(function( $ ) {
	'use strict';

	// The Application
	// ---------------

	// Our overall **AppView** is the top-level piece of UI.
	app.AppView = Backbone.View.extend({

	// Instead of generating a new element, bind to the existing skeleton of
	// the App already present in the HTML.
	el: '#main',

    initialize: function() {
      console.log('initialize');
      this.$main = this.$('#main');

      this.listenTo(app.Payments, 'reset', this.addAll)
      this.listenTo(app.Payments, 'sync', this.render);

      app.Payments.fetch();
      app.Friends.fetch();

      console.log(app.Friends.at(0));
    },

    render: function() {
		if ( app.Payments.length ) {
			this.$main.show();
			/*this.$footer.show();

			this.$footer.html(this.statsTemplate({
				completed: completed,
				remaining: remaining
			}));

			this.$('#filters li a')
				.removeClass('selected')
				.filter('[href="#/' + ( app.TodoFilter || '' ) + '"]')
				.addClass('selected'); */
		} else {
			this.$main.hide();
			this.$footer.hide();
		}

		//this.allCheckbox.checked = false;
    },

    // Add a single todo item to the list by creating a view for it, and
	// appending its element to the `<ul>`.
	addOne: function( payment ) {
		console.log("PAYMENT: ");
		console.log(payment);
		var view = new app.PaymentView({ model: payment });
		$('#todo-list').append( view.render().el );
	},

	// Add all items in the **Todos** collection at once.
	addAll: function() {
		this.$('#todo-list').html('');
		app.Payments.each(this.addOne, this);
	},

    getFriends: function ()
    {
    	console.log('get friends');
    }
  });
});
