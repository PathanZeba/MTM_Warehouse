from flask import Blueprint, render_template

# Flask Blueprint (equivalent to Controller)
account_bp = Blueprint('account_bp', __name__, url_prefix='/account')

@account_bp.route('/access_denied')
def access_denied():
    return render_template('account/access_denied.html')  # Equivalent to returning View()
