/**
 * Created by altair on 28.11.16.
 */

$('#edit_timetable_modal').on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget); // Button that triggered the modal
    let timetable = button.data('timetable'); // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    let modal = $(this);
    let form = $(modal.find('form'));
    let action_url = form.data('action-template-url').replace("0", timetable);
    form.data("action", action_url);
    $.get(action_url, {}, (data)=> {
        form.html(data);
    });
});

$('#edit_timetable_form').submit(function (event) {
    let form_page = location.href;
    let form = $(this);
    $.post(form.data("action"), form.serialize(), data => {
        console.log(data);
        if (data.length > 0) {
            form.html(data);
        } else {
            console.log("There must be reload");
            location.reload();
        }
    });
    return event.preventDefault();
});

$(".b-timetable-remove").click((event) => {
    event.preventDefault();
    console.log(event.currentTarget);
    let link = $(event.currentTarget);
    let list_group_item = $(event.currentTarget).closest(".list-group-item-with-line");
    console.log(list_group_item);
    let timetableName = $(list_group_item.find(".list-group-item-heading")).find("a").get(0);
    timetableName = $(timetableName);
    console.log(link.attr("href"));
    swal({
        title: "Are you sure?",
        text: "Вы действительно хотите удалить расписание " +
        timetableName.text() + " ?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, delete it!",
        closeOnConfirm: true
    }, function () {
        $.post(link.attr("href"), {}, (data) => {
            console.log(data);
            if (data.length == 0) {
                list_group_item.remove();
            }
        });
    });

});