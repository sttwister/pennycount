var app = app || {};

$(function() {

  Backbone.Tastypie.csrfToken = $.cookie( 'csrftoken' );

  // Kick things off by creating the **App**.
  new app.AppView();
});
