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
      this.$main = this.$('#main');
      this.$footer = this.$('#togivefooter');

      this.listenTo(app.UserPayments, 'reset', this.addAll);
      this.listenTo(app.UserPayments, 'sync', this.render);
      this.listenTo(app.GroupPayments, 'add', this.refreshPayments);
      this.listenTo(app.GroupPayments, 'remove', this.refreshPayments);

      app.UserPayments.fetch();
    },

    refreshPayments: function() {
      app.UserPayments.fetch();
    },

    render: function() {
      if ( app.UserPayments.length ) {
        this.$main.show();
        this.$footer.show();
      } else {
        this.$main.hide();
        this.$footer.hide();
      }

      this.$footer.html(this.totalTemplate({
        total: 123
      }));
    },

    // Add a single user payment item to the list by creating a view for it, and
    // appending its element to the `<ul>`.
    addOne: function( userpayment ) {
      var view = new app.UserPaymentView({ model: userpayment });
      $('#userpayment-list').append( view.render().el );
    },

    // Add all items in the **UserPayments** collection at once.
    addAll: function() {
      $('#userpayment-list').html('');
      app.UserPayments.each(this.addOne, this);
    }
  });
});
