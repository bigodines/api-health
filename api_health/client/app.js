var app = angular.module('ApiHealthApp', [
  'ngRoute',
  'TaskController'
]);

/* changes Angular default's so that it can co-exist in harmony with jinja2 :) */
app.config(function($routeProvider, $interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');

  $routeProvider
  .when('/', {
      templateUrl: '/client/templates/list.html',
      controller: 'TaskListCtrl'
    })
  .when('/task/new', {
      templateUrl: '/client/templates/new_task.html',
      controller: 'TaskCreateCtrl'
  })
  .when('/detail/:taskId', {
      templateUrl: '/client/templates/detail.html',
      controller: 'TaskDetailCtrl'
  });
});

