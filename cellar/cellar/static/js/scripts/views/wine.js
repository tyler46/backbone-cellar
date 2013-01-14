define([
    'jquery',
    'underscore',
    'mustache',
    'backbone'
], function($, _, Mustache, Backbone) {
    var WineListItemView = Backbone.View.extend({
        tagname: 'li',

        template: $('#tpl-wine-list-item').html(),
        initialize: function() {
            this.model.on('change', this.render, this);
        },

        render: function(eventName) {
            var markup = Mustache.to_html(this.template, this.model.toJSON());
            this.$el.html(markup);
            return this;
        }
    });

    return WineListItemView;
});
