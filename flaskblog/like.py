{% for post in posts %}
    {% if current_user.is_authenticated %}
        {% if current_user.has_liked_post(post) %}
            <a href="{{ url_for('like_action', post_id=post.id, action='unlike') }}">Unlike</a>
        {% else %}
            <a href="{{ url_for('like_action', post_id=post.id, action='like') }}">Like</a>
        {% endif %}
        {{ post.likes.count() }} likes
    {% else %}
        {{ post.likes.count() }} likes
    {% endif %}{% endfor %}



<--- route--->
@app.route('/like/<int:post_id>/<action>')
@login_required
def like_action(post_id, action):
    post = Post.query.filter_by(id=post_id).first_or_404()
    if action == 'like':
        current_user.like_post(post)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(post)
        db.session.commit()
    return redirect(request.referrer)

<----models---->