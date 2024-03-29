from flask import url_for
import os
from PIL import Image
from membership import app, mail
import secrets
from flask_mail import Message


def save_picture(form_picture):

    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (600, 600)
    i = Image.open(form_picture)

    #os error fix
    if i.mode != 'RGB':
      i = i.convert('RGB')

    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
  token = user.get_reset_token()
  msg = Message('Password Reset Request',
                sender='noreply@demo.com',
                recipients=[user.email])
  msg.body = f'''To reset your password, visit the following link:
{url_for('main.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
  
  try:
    mail.send(msg)
  except:
     return "Sorry, can't perform this action! Please, connect to the internet and try again."
