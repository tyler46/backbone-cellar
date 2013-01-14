define([
    'jquery',
    'underscore',
    'backbone',
    'views/wine'
], function($, _, Backbone, WineListItemView) {
    var WineListView = Backbone.View.extend({
        tagname: 'ul',

        initialize: function() {
            this.model.bind('reset', this.render, this);
        },

        render: function(eventName) {
            $(this.el).html("");
            _.each(this.model.models, function(wine){
                $(this.el).append(new WineListItemView({model:wine}).render().el);
            }, this);
            return this;
        }

    });

    return WineListView;
});
