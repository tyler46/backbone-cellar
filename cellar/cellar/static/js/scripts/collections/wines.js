define([
    'underscore',
    'backbone',
    'models/wine'
], function(_, Backbone, Wine) {
    var Wines = Backbone.Collection.extend({
        // Reference to this collection's model
        model: Wine,

        url: '/api/wines/'
    });

    return Wines;
});
