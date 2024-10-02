from flask import Flask, render_template, request
import mensagens

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #obtem o nome do formulario
        nome = request.form.get("nome") # atributo name do formulario

    #gera mensagem
    mensagem = f"Olá {nome}!\nMensagem: {mensagens.obter_mensagem_aleatoria()}"

    #Renderizar a pagina com a mensagem
    return render_template("index.html", texto=mensagem)

    #Renderiza a pagina inicial com o formulário
    return render_temnplate("index.html")

if __name__ == "__main__":
    app.run(debug=True)
