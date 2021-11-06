$('.create-classroom').click(function() {

    window.location = "create_quizroom"

})



//show the edit form when click on toggler of quizroom
$(".toggle").click(function() {
    $('.bg-modal').css('display', 'flex')

})


//hide the edit form when click on 'X' of the form
$(".close").click(function() {
    $('.bg-modal').css('display', 'none')
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
        console.log("true")
        $('.select_class select').val('3').change()
    } else {
        console.log("false")
    }
    console.log(subject_name)
    console.log(assigned_group)

})