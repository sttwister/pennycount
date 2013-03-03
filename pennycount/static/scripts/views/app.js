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

	totalTemplate: _.template( $('#total-template').html() ),

    initialize: function() {
      console.log('initialize');

      this.$main = this.$('#main');
      this.$footer = this.$('#togivefooter');

      this.listenTo(app.UserPayments, 'reset', this.addAll);
  	  this.listenTo(app.UserPayments, 'sync', this.render);

      app.UserPayments.fetch();

      this.listenTo(app.Groups, 'sync', this.printGroups);

      app.Groups.fetch();
    },

    printGroups: function() {
    	app.Groups.each(this.printGroup, this);
    },

    printGroup: function( group ) {
    	console.log('Group: ');
    	console.log(group);
    },

    render: function() {
    	console.log('render');

		if ( app.UserPayments.length ) {
			this.$main.show();
			this.$footer.show();
		} else {
			this.$main.hide();
			this.$footer.hide();
		}
    },

    // Add a single user payment item to the list by creating a view for it, and
	// appending its element to the `<ul>`.
	addOne: function( userpayment ) {
		console.log(userpayment);
		console.log(userpayment.get('value'));

		var view = new app.UserPaymentView({ model: userpayment });

		if (userpayment.get('value') < 0)
		{
			$('#user-receive-list').append( view.render().el );
		}
		else
		{
			$('#user-give-list').append( view.render().el );
		}
	},

	// Add all items in the **UserPayments** collection at once.
	addAll: function() {
		this.$('#userpayment-list').html('');
		app.UserPayments.each(this.addOne, this);
	}
  });
});
