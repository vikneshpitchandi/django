angular.module('myadminpage', []).controller('adminform_ctrl', ['$scope','$http',function($scope,$http) {
	//alert("asasa");
		$scope.post_func = function() {
			// alert("sdsd");
			 //alert($scope.mailid);
			 //alert($scope.password_data);
			                        var data = {
                            		manager_mailid:$scope.mailid,
									manager_password:$scope.password_data
                        };
                         $http.post('Manager_login', angular.toJson(data)).success(function (response) {
                           //alert(response);
                           /*$http.get('get_pred', angular.toJson(data)).success(function (response) {
                           alert(response);
                           });*/
                           if(response=='success')
                            window.location.href='http://localhost:8000/adminpage';



					});
		};
}]);


angular.module('adminpage', []).controller('add_admin_ctrl', ['$scope','$http',function($scope,$http) {

		$scope.post_func = function() {
			                        var data = { admin_id:$scope.admin_id,admin_name: $scope.admin_name,admin_designation:$scope.admin_designation,admin_mailid:$scope.admin_mailid,admin_password:$scope.admin_password };
                         $http.post('/api/add_admin/', angular.toJson(data)).success(function (response) {
                           alert(response);
                           if(response[0]=='error')
                           alert("invalid credentials");
                           else
                           //alert(JSON.stringify(response));
							return response.data
					});
		};
}]);

angular.module('adminpage').controller('add_employee_ctrl', ['$scope','$http',function($scope,$http) {

		$scope.post_func = function() {
			                        var data = { employee_id:$scope.employee_id,employee_name:$scope.employee_name,employee_designation:$scope.employee_designation,employee_mailid:$scope.employee_mailid,employee_password:$scope.employee_password };
                         $http.post('/api/add_employee/', angular.toJson(data)).success(function (response) {
                           alert(response);
                           if(response[0]=='error')
                           alert("invalid credentials");
                           else
                           //alert(JSON.stringify(response));
							return response.data
					});
		};
}]);





angular.module('Predtime', []).controller('Predtime_ctrl', ['$scope','$http',function($scope,$http) {
	//alert("asasa");
		$scope.post_func = function() {
			// alert("sdsd");
			 //alert($scope.mailid);
			 //alert($scope.password_data);
			                        var data = {
                            		quantity:$scope.t_quantity,
									type:$scope.t_type
                        };

                         $http.post('get_predtime', angular.toJson(data)).success(function (response) {

                           /*$http.get('get_pred', angular.toJson(data)).success(function (response) {
                           alert(response);
                           });*/
                           if(response=='success')
                            window.location.href='http://localhost:8000/adminpage';



					});
		};
}]);

