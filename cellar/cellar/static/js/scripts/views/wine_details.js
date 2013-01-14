define([
    'jquery',
    'underscore',
    'mustache',
    'backbone',
], function($, _, Mustache, Backbone) {
    var WineView = Backbone.View.extend({

        template: $('#tpl-wine-details').html(),

        render: function (eventName) {
            var markup = Mustache.to_html(this.template, this.model.toJSON());
            $(this.el).html(markup);
            return this;
        }
    });
    
    return WineView;
});
