//---------------------------------------------------------.
// XML Parser.
//  ./resources/text/text_en.xml が英語リソース.
//  ./resources/text/text_ja.xml が日本語リソース.
//
// 要 : ./js/readExternalFile.js
//---------------------------------------------------------.

// ----------------------------------------------.
// キー名と値の文字列リストを取得し、HTML側の名称を更新していく.
// ----------------------------------------------.
function loadTextResources ($scope, $timeout, isJapanese) {
    fileName = isJapanese ? "text_ja.xml" : "text_en.xml";
    fileStr  = readFileToString("./resources/text/" + fileName);
    if (fileStr == null) return [];
    
    var reader = new FileReader();
    reader.addEventListener('load', parseXML, false);

    var blob = new Blob([fileStr] , {type:"text/xml"});
    reader.readAsText(blob);    // 読み込み開始.

    function parseXML (e) {
        var xml = e.target.result;
        var parser = new DOMParser();
        var dom = parser.parseFromString(xml, 'text/xml');
        if (dom == null) return;

        // XMLよりIDと値の組み合わせを取得.
        var rootNode = dom.documentElement;
        if (rootNode == null) return;

        resourcesList = [];
        var objs = rootNode.getElementsByTagName("string");
        for (i = 0; i < objs.length; i++) {
            id    = objs[i].getAttribute("id");
            value = objs[i].getAttribute("value");
            resourcesList[id] = value;
        }

        // UIリソースを更新.
        updateUIText($scope, $timeout, resourcesList);

        $scope.$apply();		// AngularJSとJavaScriptのViewのバインドを更新.
    }

    //--------------------------------------------------------.
    // UIリソースを更新.
    //--------------------------------------------------------.
    function updateUIText ($scope, $timeout, resourcesList) {
        $scope.ui_msg_can_not_use_physics = resourcesList["msg_can_not_use_physics"];
        $scope.ui_msg_can_not_use_physics_grade = resourcesList["msg_can_not_use_physics_grade"];
        $scope.ui_msg_can_not_open_scene  = resourcesList["msg_can_not_open_scene"];
        $scope.ui_title                   = resourcesList["title"];
        $scope.ui_group_physics_shape     = resourcesList["group_physics_shape"];
        $scope.ui_group_calc_physics      = resourcesList["group_calc_physics"];
        $scope.ui_softbody                = resourcesList["softbody"];
        $scope.ui_second                  = resourcesList["second"];
        $scope.ui_unit_mm                 = resourcesList["unit_mm"];
        $scope.ui_param_rigid_soft        = resourcesList["param_rigid_soft"];
        $scope.ui_param_collision         = resourcesList["param_collision"];
        $scope.ui_param_margin            = resourcesList["param_margin"];
        $scope.ui_param_softbody_volume   = resourcesList["param_softbody_volume"];
        $scope.ui_param_softbody_klst     = resourcesList["param_softbody_klst"];
        $scope.ui_param_softbody_kvc      = resourcesList["param_softbody_kvc"];
        $scope.ui_param_all_pass_time     = resourcesList["param_all_pass_time"];
        $scope.ui_param_pass_time         = resourcesList["param_pass_time"];
        $scope.ui_param_stop_trigger      = resourcesList["param_stop_trigger"];
        $scope.ui_button_convert_shapes   = resourcesList["button_convert_shapes"];
        $scope.ui_button_physics_clear    = resourcesList["button_physics_clear"];
        $scope.ui_button_append           = resourcesList["button_append"];
        $scope.ui_button_update           = resourcesList["button_update"];
        $scope.ui_button_remove           = resourcesList["button_remove"];
        $scope.ui_button_cancel           = resourcesList["button_cancel"];
        $scope.ui_msg_not_number_pass_time = resourcesList["msg_not_number_pass_time"];
        $scope.ui_msg_not_number           = resourcesList["msg_not_number"];

        $scope.ui_tooltip_physics_clear          = resourcesList["tooltip_physics_clear"];
        $scope.ui_tooltip_shapes_listbox         = resourcesList["tooltip_shapes_listbox"];
        $scope.ui_tooltip_rigid_soft_static      = resourcesList["tooltip_rigid_soft_static"];
        $scope.ui_tooltip_rigid_soft_dynamic     = resourcesList["tooltip_rigid_soft_dynamic"];
        $scope.ui_tooltip_rigid_soft_softbody    = resourcesList["tooltip_rigid_soft_softbody"];
        $scope.ui_tooltip_collision_sphere       = resourcesList["tooltip_collision_sphere"];
        $scope.ui_tooltip_collision_box          = resourcesList["tooltip_collision_box"];
        $scope.ui_tooltip_collision_capsule      = resourcesList["tooltip_collision_capsule"];
        $scope.ui_tooltip_collision_mesh         = resourcesList["tooltip_collision_mesh"];
        $scope.ui_tooltip_margin                 = resourcesList["tooltip_margin"];
        $scope.ui_tooltip_softbody_volume        = resourcesList["tooltip_softbody_volume"];
        $scope.ui_tooltip_softbody_klst          = resourcesList["tooltip_softbody_klst"];
        $scope.ui_tooltip_softbody_kvc           = resourcesList["tooltip_softbody_kvc"];
        $scope.ui_tooltip_append_shapes          = resourcesList["tooltip_append_shapes"];
        $scope.ui_tooltip_update_shapes          = resourcesList["tooltip_update_shapes"];
        $scope.ui_tooltip_remove_shapes          = resourcesList["tooltip_remove_shapes"];
        $scope.ui_tooltip_all_pass_time          = resourcesList["tooltip_all_pass_time"];
        $scope.ui_tooltip_pass_time              = resourcesList["tooltip_pass_time"];
        $scope.ui_tooltip_stop_trigger           = resourcesList["tooltip_stop_trigger"];
        $scope.ui_tooltip_time_reset             = resourcesList["tooltip_time_reset"];
        $scope.ui_tooltip_time_prev              = resourcesList["tooltip_time_prev"];
        $scope.ui_tooltip_time_next              = resourcesList["tooltip_time_next"];
        $scope.ui_tooltip_conv_shapes            = resourcesList["tooltip_conv_shapes"];
        $scope.ui_tooltip_cancel                 = resourcesList["tooltip_cancel"];
    }
}
