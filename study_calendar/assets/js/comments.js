/**
 * Created by altair on 29.11.16.
 */

$("#comment_add_form").submit(function(event) {
    event.preventDefault();
    let form = $(this);
    let comments = $("#comments_list");
    console.log(form.attr("action"));
    $.post(form.attr("action"), form.serialize(), (data) => {
        comments.append(data);
    });
});