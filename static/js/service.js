Blog.service('AppService', AppService);

function AppService($http){

    return {
        getRestaurant : getRestaurant,
        getComments : getComments
    }

    function getRestaurant(){
        return $http.get('/api/restaurants/');
    }
    function getComments(){
        return $http.get('/api/comments/');
    }
}
