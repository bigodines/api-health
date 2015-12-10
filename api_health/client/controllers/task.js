'use strict';

var taskController = angular.module('TaskController', ['TaskService']);

taskController.controller('TaskListCtrl', function($scope, Task) {
    $scope.all_tasks = Task.query();
});

taskController.controller('TaskCreateCtrl', function($scope, $routeParams, $location, Task) {
    $scope.task = new Task();
    $scope.save = function() {
        $scope.task.$save(function() {
            $location.path('/');
        })
    }

});

taskController.controller('TaskDetailCtrl', function($scope, $routeParams, Task) {
    var taskId  = $routeParams.taskId;
    $scope.task = Task.query({taskId: taskId});
});
