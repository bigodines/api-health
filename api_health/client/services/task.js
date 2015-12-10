'use strict';

var service = angular.module('TaskService', ["ngResource"]);

service.factory('Task', function($resource) {
    var Task = $resource("/api/task");
    return Task;
});

