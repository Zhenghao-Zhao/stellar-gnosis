/************** click anywhere on page to cancel popups **************/
$(document).click(function (e) {
    var container = $(".popup");
    // if the target of the click isn't the container nor a descendant of the container.
    if (!$(".more_vert").is(e.target) && container.has(e.target).length === 0) {
        container.attr('hidden', true);
    }
});

var this_comment;

/************** toggles more button: shows/hides popup menu **************/
function toggle_more(ele) {
    var hidden = $(ele).siblings('.popup').attr('hidden');
    $('.popup').attr('hidden', true);
    $(ele).siblings('.popup').attr('hidden', !hidden);
    this_comment = $(ele).closest('#comment_thread');
}

/************** opens flag dialog that contains flag form **************/
function open_flag_dialog(comment_id) {
    // hide all current popups
    $('.popup').attr('hidden', true);
    $('#flag_form_container').attr('hidden', false);

    // add comment id to the form
    $("<input />").attr("type", "hidden")
        .attr("name", "comment_id")
        .attr("value", comment_id)
        .appendTo("#flag_form");
}

/************** hide popup form and reset its text. **************/
function cancel_form() {
    $('#flag_form').trigger('reset');
    $('.popup').attr('hidden', true);
}

$('.show_comment').click(function () {
    console.log("this is called!");
    var $hidden = $(this).closest('#hidden_comment');

    this_comment = $hidden.next('#comment_thread');
    if (this_comment != null) {
        $hidden.attr('hidden', true);
        $(this_comment).attr('hidden', false);
    }
});

/************** sending ajax post request with flag forms **************/
var form = $('#flag_form');
form.submit(function (e) {
    e.preventDefault();

    $('.popup').attr('hidden', true);

    // open loader
    $('#loader').attr('hidden', false);

    $.ajax({
        type: 'POST',
        url: window.location.href,
        data: form.serialize(),
        success: function (data) {
            console.log("submit successful!");

            if (this_comment != null) {
                $(this_comment).attr('hidden', true);
                $(this_comment).prev('#hidden_comment').attr('hidden', false);
            }

            $('#flag_form').trigger('reset');
            // close loader
            $('#loader').attr('hidden', true);
            $('#flag_response').attr('hidden', false);
        },
        error: function (data) {
            $('#loader').attr('hidden', true);
            alert("An error has occurred, please resubmit report.");
        },

    })
});