'use strict';

var taskController = angular.module('TaskController', ['TaskService']);

taskController.controller('TaskListCtrl', function($scope, Task) {
    $scope.all_tasks = Task.query();
});
