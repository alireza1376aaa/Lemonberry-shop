function getcode() {
    var getcode = $('#verify_code_box').val()
    var x = '@Session["email"]'
    console.log(x)
    if (getcode.length >= 5) {
        $.ajax({
            method: 'POST',
            url: '/user/register',
            data: {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(), 'code': getcode},
            success: function (res) {
                window.location.replace("/user/edit");
            },
            error: function (res) {
                $('#massage_very1').text('کد وارد شده صحیح نمیباشد').addClass('text-danger')
            }
        })
    }
}

function sendagain() {
    var code_again = 'True'
    $.ajax({
        method: 'GET',
        url: '/user/register',
        data: {'again': code_again},
        success: function () {
            code_again = 'False'
            $('#massage_very2').text('با موفقیت پیام دوباره ارسال شد').addClass('text-success')
            delayedLoop();
        }
    })
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah').attr('src', e.target.result).width(150).height(200);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function remove_filter() {
    var filter = window.location.href.split("?")
    console.log()
    if (filter.length === 2) {
        window.location.replace(filter[0]);
    } else {
    }

}

function get_comment(id) {

    var parent = $("#parent_id_val").val(id)
    document.getElementById('form_comment').scrollIntoView({behavior: "smooth"});
}

$(document).ready(function () {
    $('#select-by-size').change(function () {
        var selectedOption = $('#select-by-size option:selected').val();
        var product_id = $('#product_my_id').val()
        $.ajax({
            method: 'GET',
            url: '/product/get_color_product',
            data: {'count_repo': selectedOption, 'product_id': product_id},
            success: function (res) {
                $('#select-by-color').html(res)
            }
        })
    });
})


function basket_click() {
    var color = $("#select-by-color").val()
    var size = $("#select-by-size").val()
    if (color !== null && size !== null) {
        $("#cart_form_sub").submit()
    } else {
        $("#error_text_size_color").text('ابتدا سایز و رنگ محصول را انتخاب کنید')
    }
}


function changeOrderDetailCount(product_id_change,status) {
    $.get('change-order-detail?detail_id=' + product_id_change + '&status=' + status ).then(res => {
        $('#reza').html(res.body);
    });
}
