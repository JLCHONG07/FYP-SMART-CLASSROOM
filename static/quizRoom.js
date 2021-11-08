//--------------------Admin-------------------------------------//
//click on create a quizroom will point to create_quizroom url
$('.create-classroom').click(function() {
    window.location = "create_quizroom"
})

//show the edit form when click on toggler of quizroom
$(".toggle").click(function() {
    $('.bg-modal').css('display', 'flex')

})

//hide the edit form when click on 'X' of the form
$(".close").click(function() {
    //default all texts
    $('.bg-modal').css('display', 'none')
    $('.form .hidden-delete-confirmation .invalid-input').css("display", "none")
    $('.hidden-delete-confirmation').css('display', 'none')
    $('.form .form-group .invalid-input').css('display', 'none')
    $('.form .form-group .select_class .invalid-input').css('display', 'none')

    //----student join room---//
    $('.join-quizroom-modal').css('display', 'none')
})

//show the delete confirm msg when click on toggler of quizroom
$("button.delete").click(function() {
    $('.hidden-delete-confirmation').css('display', 'flex')

})

//show the delete confirm msg when click on toggler of quizroom
$("button.cancel").click(function() {
    $('.hidden-delete-confirmation').css('display', 'none')

})


//Get the id and name of quizroom when onclick
$(".card").click(function() {
    //Used for get the id and pass to backend
    var id = $(this).find('.hidden-id').text()
    $('#hidden-field-id-input').val(id).trigger("change")
        //Applied to "Select Your Quiz Room"
    var subject_name = $(this).find('.quiz-title-name').text()
    $('#subject-name').val(subject_name).trigger("change")

})

//Get the subject of quizroom when onclick
$(".card").click(function() {
    var subject_name = $(this).find('.quiz-title-name').text()
    $('#hidden-edit-form-subject-name').val(subject_name).trigger("change")
    var assigned_group = $(this).find('.group-assigned-name').text()
    if (assigned_group === "Assign to :Edit to select group to assign") {
        //console.log("true")
        $('.select_class select').val('0').change()
    } else if (assigned_group === "Assign To: Group 1") {
        //console.log(assigned_group)
        $('.select_class select').val('1').change()
    } else if (assigned_group === "Assign To: Group 2") {
        //console.log(assigned_group)
        $('.select_class select').val('2').change()
    } else if (assigned_group === "Assign To: Group 3") {
        //console.log(assigned_group)
        $('.select_class select').val('3').change()
    } else {
        //console.log("Invalid Input")
    }
    var id = $(this).find('.hidden-id').text()
    $('#edit-hidden-field-id-input').val(id).trigger("change")
        //console.log(subject_name)
        //console.log(assigned_group)
        //console.log(id)
})

//Show invalid message when entered not a Confirm message
$("#delete-confirmation").focus(function() {
    if ($(this).val() !== "Confirm" || $(this).val().length === 0) {
        $('.form .hidden-delete-confirmation .invalid-input').css("display", "flex")
        $('#confirm-button').attr("type", "button")
    } else {
        $('.form .hidden-delete-confirmation .invalid-input').css("display", "none")
        $('#confirm-button').attr("type", "submit")
    }
})
$('#delete-confirmation').keyup(function() {
    if ($(this).val() !== "Confirm" || $(this).val().length === 0) {
        $('.form .hidden-delete-confirmation .invalid-input').css("display", "flex")
        $('#confirm-button').attr("type", "button")
    } else {
        $('.form .hidden-delete-confirmation .invalid-input').css("display", "none")
        $('#confirm-button').attr("type", "submit")
    }
})

//invalid the confirm button when "Confirm" word not entered
$('#confirm-button').click(function() {
    var button_attr = $('#confirm-button').attr("type")
        //console.log(button_attr)
    if (button_attr === "button") {
        $('.form .hidden-delete-confirmation .invalid-input').css("display", "flex")
    }
})


//Invalid the submit button to edit when the subject or assign to is blank
$('#edit-button').click(function() {
    var subject = $.trim($('#hidden-edit-form-subject-name').val()).length
    var assign_group = $('#hidden-edit-form-group-assigned').val()
    console.log(subject)
    console.log(assign_group)
        //if subject name and assign_group is entered and selected
    if (subject > 0 && assign_group !== "0") {
        $('#edit-button').attr('type', 'submit')
    }
    if (subject === 0) {
        $('.form .form-group .invalid-input').css('display', 'flex')
    } else {
        $('.form .form-group .invalid-input').css('display', 'none')
    }

    if (assign_group === "0") {
        $('.form .form-group .select_class .invalid-input').css('display', 'flex')
    } else {
        $('.form .form-group .select_class .invalid-input').css('display', 'none')
    }

})

//---------------------------------------------------------------------------------//
//-------------------------Student------------------------------------------------//
$(".join-classroom ").click(function() {
    $('.join-quizroom-modal').css('display', 'flex')
})

//Invalid the submit button to edit when the subject or assign to is blank
$('#join-button').click(function() {

    if ($('#join-quiz-code').val() >= 100000 && $('#join-quiz-code').val().length >= 0 && $('#join-quiz-code').val().length <= 6 && $('#join-quiz-code').val() <= 999999) {

        $('#join-button').attr("type", "submit")
            //window.location = "joinQuizroom"

    } else {
        $('#join-button').attr("type", "button")
        $('.form .hidden-join-confirmation .invalid-input').css("display", "flex")

    }
})


/*
 $("#confirm-join-button").click(function(){

})*/