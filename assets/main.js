$(document).ready(function () {

            $(".pill-nav a").click(function () {
                var id = $(this);

                $(".pill-nav a").removeClass("active");
                $(id).addClass("active");
                localStorage.setItem("selectedolditem", $(id).text());
            });

            var selectedolditem = localStorage.getItem('selectedolditem');
            if (selectedolditem !== null) {
                $("a:contains('" + selectedolditem + "')").addClass("active");
            }
        });



function openForm() {
  document.getElementById("myForm").style.display = "block";
};



function showalert() {
    document.getElementById("alertdiv").style.visibility="visible";
}
    setTimeout("showalert()", 4000);


$(document).ready(function () {
    $('#remind').click(function () {
        $('#alertid').show('fade');

        setTimeout(function () {
            $('#alertid').hide('fade');
        }, 4000);
    });

    $('#remindClose').click(function () {
        $('#alertid').hide('fade');
    });
});


/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}
