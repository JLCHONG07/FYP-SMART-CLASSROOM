//Get the id and name of quizroom when onclick
$(".table-list-content").click(function() {
    //Used for get the id and pass to backend
    var id = $(this).find('.question-id').text()
    $('#hidden-field-id-input').val(id).trigger("change")
        //Applied to "Select Your Quiz Room"
    var question = $(this).find('.question-list').text()
    $('#question-list-question').val(question).trigger("change")

})