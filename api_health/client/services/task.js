'use strict';

var service = angular.module('TaskService', ["ngResource"]);

service.factory('Task', function($resource) {
    var Task = $resource("/api/task/:taskId",
            {taskId: '@id'},
            {
                save: {
                    method: 'POST',
                    url: "/api/task",
                    transformRequest: function(data, headers) {
                        headers = angular.extend({}, headers, {'Content-Type': 'application/json'});
                        return angular.toJson(data); // this will go in the body request
                    }
                }

            });
    Task.prototype.isNew = function(){
            return (typeof(this.id) === 'undefined');
        }
    return Task;
});

