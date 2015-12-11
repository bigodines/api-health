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

taskController.controller('TaskDetailCtrl', function($scope, $routeParams, $location, Task) {
    var taskId  = $routeParams.taskId;
    $scope.task = Task.get({id: taskId});
    $scope.update = function() {
        $scope.task.$update(function() {
            $location.path('/');
        })
    }
});
