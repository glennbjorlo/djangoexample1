

$(document).ready(function(){


    $("#increase_passed_exams_button").click(function(event) {
        event.preventDefault();
        $.ajax({
            url: $('#passed_exams_url').val()
        })
        .done(function(data){
            var passed_exams_updated = data['passed_exams_updated'];
            $("#passed_exams_cell").html(passed_exams_updated);
        });
    });

	$("#increase_nr_of_courses_button").click(function(event) {
		event.preventDefault();
		$.ajax({
			url: $('#nr_courses_url').val()
		})
		.done(function(data) {
			var nr_courses_updated = data['number_of_courses'];
			$("#nr_courses_cell").html(nr_courses_updated);
		});

	});

	$("#decrease_nr_of_courses_button").click(function(event) {
		event.preventDefault();
		$.ajax({
			url: $('#de_nr_courses_url').val()
		})
		.done(function(data) {
			var nr_courses_updated = data['number_of_courses'];
			$("#nr_courses_cell").html(nr_courses_updated);
		});

	});




});

