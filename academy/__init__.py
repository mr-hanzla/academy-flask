from flask import (
    Blueprint,
    render_template,
    url_for
)

bp = Blueprint('academy', __name__)

@bp.route('/academy')
def index():
    return render_template('academy/mainpage.html')

