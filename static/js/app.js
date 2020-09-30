'use strict';

var Blog = angular.module("Blog", ["ui.router", "ui.bootstrap", "ngCookies"], function ($interpolateProvider) {
         $interpolateProvider.startSymbol("{[{");
         $interpolateProvider.endSymbol("}]}");
     }
);


Blog.run(function ($http, $cookies) {
     $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
})


Blog.config(function ($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/restaurants');
    $stateProvider.state('restaurants',{
        url : '/restaurants',
        templateUrl : '/static/index.html',
        title : 'Restaurant',
        controller:'RestaurantController'
    })
    $stateProvider.state('comments',{
        url : '/comments/{id}',
        templateUrl : '/static/subpage.html',
        title : 'Comments',
        controller:'CommentController'
    })
});