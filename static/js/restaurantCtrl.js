var restaurantController = Blog.controller('RestaurantController', function ($scope, $rootScope, AppService) {
     AppService.getRestaurant().then(function(response){
            $scope.restaurant = response.data;
        }, function(response){
            console.error("Error getting restaurant", response);
        });
});