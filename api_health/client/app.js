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
    });
});

