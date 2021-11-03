//select admin or student login and change color of "Student" or "Admin words"
$(".navbar-words").click(function(e) {
    $(".navbar-words").removeClass("active");
    $(this).addClass("active")
})


function logout() {
    var txt = confirm("Are You Sure Want to Logout?");
    if (txt) {
        // console.log("logout");

        window.location = "logout";
    } else {
        // console.log("Action canceled");
    }

}