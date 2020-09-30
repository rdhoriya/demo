var commentController = Blog.controller('CommentController', function ($scope, $rootScope, $stateParams, AppService) {
     console.log($stateParams.id)
     AppService.getComments().then(function(response){
            $scope.comments = response.data;
        }, function(response){
            console.error("Error getting comments", response);
        });
});