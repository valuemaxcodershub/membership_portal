from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from membership.models import User


class MessageForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(), Length(min=0, max=140)])
    message = TextAreaField('Message', validators=[
        DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('Submit')

class UploadCsvForm(FlaskForm):
  csv_file = FileField('Upload CSV file', validators=[DataRequired(), FileAllowed(['csv',])])
  submit = SubmitField("Submit")


class UnitRegistrationForm(FlaskForm):
  name = StringField("Unit name", validators=[DataRequired(), Length(min=2,max=30)])
  submit = SubmitField("Submit")


class AdminRegistrationForm(FlaskForm):
  email = StringField("Email", validators=[DataRequired(), Email()])
  is_superadmin = BooleanField("Add as a super administrator")
  submit = SubmitField("Add Member")

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('That username is taken. Please choose a different one.')

  def validate_email(self, email):
    user = User.query.filter_by(business_email=email.data).first()
    if user:
      raise ValidationError('That email is taken. Please choose a different one.')

  def validate_phone(self, phone):
    user = User.query.filter_by(business_phone=phone.data).first()
    if user:
      raise ValidationError('That phone number is taken. Please choose a different one.')


class UserRegistrationForm(FlaskForm):
  
  phone = StringField(validators=[DataRequired()])
  submit = SubmitField("Add Member")

  def validate_phone(self, phone):
    user = User.query.filter_by(business_phone=phone.data).first()
    if user:
      raise ValidationError('That phone number is taken. Please choose a different one.')



class AdminLoginForm(FlaskForm):
  email = StringField(validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  remember = BooleanField("Remember me")
  submit = SubmitField("Log In")


#try fixing no update using init
class UpdateMemberForm(FlaskForm):

  email = StringField("Email", validators=[DataRequired(), Email()])
  picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
  phone = StringField(validators=[DataRequired()])
  password = StringField("Password", validators=[DataRequired()])
  business_name = StringField()
  business_about = StringField()
  business_address = StringField()
  # business_phone = StringField()
  date_of_birth = StringField()
  # business_email = StringField()
  submit = SubmitField("Edit Member")
  current_member = None

  def validate_username(self, username):
    if username.data != self.current_member.username:
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError('That username is taken. Please choose a different one.')

  def validate_email(self, email):
    if email.data != self.current_member.business_email:
      user = User.query.filter_by(business_email=email.data).first()
      if user:
        raise ValidationError('That email is taken. Please choose a different one.')

  def validate_phone(self, phone):
    if phone.data != self.current_member.business_phone:
      user = User.query.filter_by(business_phone=phone.data).first()
      if user:
        raise ValidationError('That phone number is taken. Please choose a different one.')


class UpdateAdminForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=2,max=20)])
  email = StringField("Email", validators=[DataRequired(), Email()])
  picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
  phone = StringField(validators=[DataRequired()])
  password = StringField("Password", validators=[DataRequired()])
  submit = SubmitField("Edit Member")
  current_member = None

  def validate_username(self, username):
    if username.data != self.current_member.username:
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError('That username is taken. Please choose a different one.')

  def validate_email(self, email):
    if email.data != self.current_member.business_email:
      user = User.query.filter_by(business_email=email.data).first()
      if user:
        raise ValidationError('That email is taken. Please choose a different one.')

  def validate_phone(self, phone):
    if phone.data != self.current_member.business_phone:
      user = User.query.filter_by(business_phone=phone.data).first()
      if user:
        raise ValidationError('That phone number is taken. Please choose a different one.')
