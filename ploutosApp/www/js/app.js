// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.controllers' is found in controllers.js
angular.module('starter', ['ionic', 'starter.controllers', 'chart.js', 'ionic.contrib.frostedGlass'])

.run(function($ionicPlatform) {
     $ionicPlatform.ready(function() {
                          // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
                          // for form inputs)
                          if (window.cordova && window.cordova.plugins.Keyboard) {
                          cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
                          cordova.plugins.Keyboard.disableScroll(true);
                          
                          }
                          if (window.StatusBar) {
                          // org.apache.cordova.statusbar required
                          StatusBar.styleDefault();
                          }
                          });
     })



.config(function($stateProvider, $urlRouterProvider) {
        $stateProvider
        
        .state('app', {
               url: '/app',
               abstract: true,
               templateUrl: 'templates/menu.html',
               controller: 'MenuCtrl'
               })
        
        
        
        
        
        .state('new-login', {
               url: '/new-login',
               templateUrl: 'templates/new-login.html',
               controller: 'LoginCtrl'
               })
        
        

        
        .state('app.dialog', {
               url: '/dialog',
               views: {
               'menuContent': {
               templateUrl: 'templates/dialog.html',
               controller: 'DialogCtrl'
               }
               }
               })
        
        
        .state('app.search', {
               url: '/search',
               views: {
               'menuContent': {
               templateUrl: 'templates/search.html'
               }
               }
               })
        
        .state('app.main', {
               url: '/main',
               views: {
               'menuContent': {
               templateUrl: 'templates/main.html',
               controller: 'ChartCtrl'
               }
               }
               })
        
        .state('app.browse', {
               url: '/browse',
               views: {
               'menuContent': {
               templateUrl: 'templates/browse.html',
               controller: 'BrowseCtrl'
               }
               }
               })
        
        .state('app.alerts', {
               url: '/alerts',
               views: {
               'menuContent': {
               templateUrl: 'templates/alerts.html',
               controller: 'AlertsCtrl'
               }
               }
               })
        
        .state('app.accounts', {
               url: '/accounts',
               views: {
               'menuContent': {
               templateUrl: 'templates/accounts.html',
               controller: 'AccountsCtrl'
               }
               }
               })
        
        
        .state('app.friends', {
               url: '/friends',
               views: {
               'menuContent': {
               templateUrl: 'templates/friends.html',
               controller: 'FriendsCtrl'
               }
               }
               })
        
        
        .state('app.achievements', {
               url: '/achievements',
               views: {
               'menuContent': {
               templateUrl: 'templates/achievements.html',
               controller: 'AchievementsCtrl'
               }
               }
               })
        
        
        .state('app.budget', {
               url: '/budget',
               views: {
               'menuContent': {
               templateUrl: 'templates/budget.html',
               controller: 'BudgetCtrl'
               }
               }
               })
        
        
        
        .state('app.alert', {
               url: '/alerts/:alertId',
               views: {
               'menuContent': {
               templateUrl: 'templates/alert.html',
               controller: 'AlertCtrl'
               }
               }
               })

        
        .state('app.friend', {
               url: '/friends/:friendId',
               views: {
               'menuContent': {
               templateUrl: 'templates/friend.html',
               controller: 'FriendCtrl'
               }
               }
               })
        
        
        .state('app.playlists', {
               url: '/playlists',
               views: {
               'menuContent': {
               templateUrl: 'templates/playlists.html',
               controller: 'PlaylistsCtrl'
               }
               }
               })

        
        .state('app.single', {
               url: '/playlists/:playlistId',
               views: {
               'menuContent': {
               templateUrl: 'templates/playlist.html',
               controller: 'PlaylistCtrl'
               }
               }
               
               
               });
        
        // if none of the above states are matched, use this as the fallback
        //$urlRouterProvider.otherwise('/app/playlists');
        $urlRouterProvider.otherwise('/new-login');
        });
