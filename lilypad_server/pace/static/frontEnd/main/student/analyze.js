// parent controller for analyze
app.controller('MainStudentAnalyzeCtrl', function ($scope) {
    $scope.views = [
        {name: 'Treatment Period', url: '/static/frontend/main/student/analyze/treatmentPeriod.html'},
        {name: 'Behavior Log', url: '/static/frontend/main/student/analyze/behaviorLog.html'},
        {name: 'Attendance Records', url: '/static/frontend/main/student/analyze/attendanceLog.html'}
    ];
});