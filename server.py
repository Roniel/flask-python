from flask import Flask, render_template, session,request,redirect
from flask_session import Session
import requests

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#HOMOLOGAÇÃO - Endereço para validar o token do link
end_point_sgr="https://homsgrapi.azurewebsites.net/api/validar-token/"

@app.route('/')
def index():
  if not session.get("nome"):
    return render_template('acesso-negado.html')
  
  return redirect("/dashboard")

# Autentica usuário no python via sessão do flask
@app.route('/auth')
def auth():
  token = request.args['token']
  response = requests.get(end_point_sgr + token)

  if response.status_code == 200:
    json_data = response.json()
    
    session["regional"] = json_data["regional"]
    session["nome"]  = json_data["nome"]

    return redirect("/dashboard")
  else:
    return render_template('acesso-negado.html')


@app.route('/acesso-negado')
def acessoNegado():
  return render_template('acesso-negado.html')

@app.route('/dashboard')
def dashboard():
  if not session.get("nome"):
    return render_template('acesso-negado.html')
  
  return render_template('dashboard.html',  name= session.get("nome") )
 

if __name__ == '__main__':
  app.run(host='localhost', threaded=True)
