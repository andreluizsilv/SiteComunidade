from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome do Usuário', validators=[DataRequired()])
    email =StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confimacao_senha = PasswordField('Confimação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')

