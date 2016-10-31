/**
 * Created by altair on 30.10.16.
 */
$.material.init()

$('#edit_timetable_modal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var timetable = button.data('timetable') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)
    var form = modal.find('form')
    var action_url = form.data('action-template-url')
    form.attr("action", action_url.replace("0", timetable))
})