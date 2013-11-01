app.controller('LoginPromptCtrl', function ($scope, authManager, mainViewState, classroomDataStore, mixpanel) {
    /** $scope interface **/

    $scope.login = {};
    $scope.authenticated = false;

    $scope.logIn = logIn;
    $scope.logOut = logOut;

    // uncomment to auto-login. 'feeny' has 3 classrooms in the dev fixture, 'turner' has only 1
    // $scope.login = {
    //     '$valid': true,
    //     'username': 'turner',
    // };
    // $scope.logIn();

    /** Implementation details **/

    function logIn() {
        if ($scope.login.$valid) {
            $scope.authenticated = authManager.authenticate($scope.login.username, $scope.login.password);

            if ($scope.authenticated) {
                initializeClassroomList();
                // mixpanel tracking
                mixpanel.track("Logged in");
            }
            else {
                console.log('invalid credentials');
                // TODO: display something about invalid credentials?
            }
        }
    }

    function logOut() {
        $scope.authenticated = false;
        $scope.login.username = null;
        $scope.login.password = null;
        mainViewState.selectedStudent = null;
        mainViewState.selectedClassroom = null;
    }

    $scope.$on('logOut', function() {
        logOut();
    });

    function initializeClassroomList() {
        // query the server for classrooms accessible by the current user and
        // handle async response with success/error callbacks
        classroomDataStore.getAll().then(
            function(classroomCollection) {
                if (classroomCollection.length === 0) {
                    // TODO
                    console.log('no classrooms found for user');
                }
                else if(classroomCollection.length === 1) {
                    console.log('classroom auto-selected: only one option available for user');
                    // skip the classroom list setup and set the selected one immediately
                    var onlyClassroom = classroomCollection.models[0];
                    mainViewState.selectedClassroom = onlyClassroom;
                }
                else {
                    // TODO: need to prompt user to select classroom (this is just a stub
                    //  that auto-selects the first classroom in the collection)
                    console.log('select a classroom (' + classroomCollection.length + ' found)');
                    var randomClassroom = classroomCollection.models[0];
                    mainViewState.selectedClassroom = randomClassroom;
                }
            },
            function(err) {
                // TODO: handle a problem getting the user's classroom list
                console.error('error fetching classroom list');
            }
        );
    }
});