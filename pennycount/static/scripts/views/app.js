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

		// Our template for the line of statistics at the bottom of the app.
		friendTemplate: _.template( $('#friend-template').html() ),

    initialize: function() {
      console.log('initialize');
      this.render();
    },

    render: function() {
      console.log('render');
    }
  });
});
