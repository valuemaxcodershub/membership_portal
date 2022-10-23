from flask import Blueprint, render_template, redirect, url_for, flash, request
from membership.members.forms import UserLoginForm
from membership.models import User
from flask_login import login_user, current_user, logout_user, login_required
from membership.members.utils import user_role_required

members = Blueprint('members', __name__)


@members.route("/member-home", methods=["GET", "POST"])
def member_home():
  if current_user.is_authenticated:
    if current_user.role == "ADMIN":
      return redirect(url_for("members.login"))

  return "Member Homepage"


@members.route("/login", methods=["GET", "POST"])
def login():
  if current_user.is_authenticated:
      if current_user.role == "USER":
        return redirect(url_for('members.member_home'))

  form = UserLoginForm()


  if request.method == "POST":
    phone_input = request.form['phone']
    password_input = request.form['password']
    user = User.query.filter_by(phone=phone_input).first()
    if user and user.password == password_input:
      login_user(user)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('members.user_account'))
    else:
      flash('Login Unsuccessful. Please check Phone number and password', 'danger')
    
  return render_template("user_login.html", title="Login", form=form)


@members.route("/account") 
@login_required
def user_account():
  if current_user.role == "USER":
    return render_template("user_account.html")
  else:
    return redirect(url_for("members.member_home"))

@members.route("/user-logout")
def user_logout():
    logout_user()
    return redirect(url_for('members.login'))

# @members.route("/edit-business-profile")
# @user_role_required
# @login_required
# def edit_business_profile():
#   # members = User.query.filter_by(role="USER").all()
#   if request.method == "POST":
#     member.business_name = request.form['username']
#     member.business_email = request.form['email']
#     member.business_phone = request.form["phone"]
#     member.business_about = request.form["business_about"]
#     member.business_services = request.form["business_services"]
#     member.business_facebook = request.form["business_facebook"]
#     member.business_twitter = request.form["business_twitter"]
#     member.business_linkedin = request.form["business_linkedin"]
#     member.business_whatsapp = request.form["business_whatsapp"]

#     image_str_list = []
#     images = request.files.getlist('images')
    
#     for image in images:
#       if image:
#         picture_file = save_picture(image)
#         image_str_list.append(picture_file)
    
#     member.business_images =  image_str_list


#   return render_template("business-profile-form.html")