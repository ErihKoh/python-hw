from flask import render_template, flash, url_for, redirect, request
from ..app import db, mail
from flask_login import login_required, current_user
from .forms import ContactForm
from ..models import Contact
from werkzeug.exceptions import abort
from .app import contact_bp
from flask_mail import Message


@contact_bp.route('/')
def about():
    return render_template('about.html')


@contact_bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(name=form.name.data, phone=form.phone.data, address=form.address.data, email=form.email.data,
                          author=current_user)
        db.session.add(contact)
        db.session.commit()
        flash('You have a new contact')
        return redirect(url_for('contacts.index'))

    contacts = Contact.query.filter_by(author=current_user).all()
    return render_template('index.html', title='home page', form=form, contacts=contacts)


@contact_bp.route('/index/<int:contact_id>')
@login_required
def contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return render_template('contact.html', contact=contact)


@contact_bp.route('/index/<int:contact_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contacts.index'))


@contact_bp.route('/index/<int:contact_id>/update', methods=['GET', 'POST'])
@login_required
def update_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    if contact.author != current_user:
        abort(404)
    form = ContactForm()
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.phone = form.phone.data
        contact.address = form.address.data
        contact.email = form.email.data
        db.session.commit()
        flash('Your contact has been update', 'success')
        return redirect(url_for('contacts.contact', contact_id=contact.id))
    form.name.data = contact.name
    form.phone.data = contact.phone
    form.address.data = contact.address
    form.email.data = contact.email

    return render_template('index.html', form=form)


@contact_bp.route('/index/<int:contact_id>/email', methods=['GET', 'POST'])
@login_required
def send_email(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    if contact.author != current_user:
        abort(403)
    msg = Message('Your contact', recipients=[current_user.email],
                  body=str(contact))
    mail.send(msg)
    flash('Your contact has been send', 'success')
    return render_template('email.html')
