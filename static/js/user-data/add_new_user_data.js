var send_data = {}

$(document).ready(function () {

    $('#id_present_division').on('change', function () {
       var selected_value = $(this).val();
       getDistricts(selected_value, '#id_present_district');
    });

    $('#id_present_district').on('change', function () {
       var selected_value = $(this).val();
       getThanaList(selected_value, '#id_present_thana');


    });

    $('#id_present_thana').on('change', function () {
       var selected_value = $(this).val();
       getUnionList(selected_value, '#id_present_post_office');


    });


    $('#id_permanent_division').on('change', function () {
       var selected_value = $(this).val();
       getDistricts(selected_value, '#id_permanent_district');
    });

    $('#id_permanent_district').on('change', function () {
       var selected_value = $(this).val();
       getThanaList(selected_value, '#id_permanent_thana');
    });

    $('#id_permanent_thana').on('change', function () {
       var selected_value = $(this).val();
       getUnionList(selected_value, '#id_permanent_post_office');

    });




})


function getDistricts(division_id, select_id) {
    let url = '/geo-data-bd/get-district-by-division';
    $.ajax({
        method: 'GET',
        url: url,
        data: {
            'division_id': division_id
        },
        beforeSend: function(){

        },
        success: function (result) {

            districts_option = "<option value='' selected>--Select--</option>";
            $.each(result, function (a, b) {
                //districts_option += "<option>" + b.name + "</option>"
                districts_option += "<option value='" + b.id + "'>" + b.name + "</option>"

            });
            $(select_id).html(districts_option)
        },
        error: function (response) {
        }
    });
}

function getThanaList(district_id, select_id) {
    let url = '/geo-data-bd/get-thana-by-district';
    $.ajax({
        method: 'GET',
        url: url,
        data: {
            'district_id': district_id
        },
        beforeSend: function(){

        },
        success: function (result) {

            thana_option = "<option value='' selected>--Select--</option>";
            $.each(result, function (a, b) {
                thana_option +=  "<option value='" + b.id + "'>" + b.name + "</option>"
            });
            $(select_id).html(thana_option)
        },
        error: function (response) {

        }
    });
}


function getUnionList(thana_id, select_id) {
    let url = '/geo-data-bd/get-union-by-thana';
    $.ajax({
        method: 'GET',
        url: url,
        data: {
            'thana_id': thana_id
        },
        beforeSend: function(){

        },
        success: function (result) {
            //console.log(result);
            union_option = "<option value='' selected>--Select--</option>";
            $.each(result, function (a, b) {
                union_option +=  "<option value='" + b.id + "'>" + b.name + "</option>"
            });
            $(select_id).html(union_option)
        },
        error: function (response) {

        }
    });
}

