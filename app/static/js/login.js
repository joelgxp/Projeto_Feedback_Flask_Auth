const formNovaConta = document.getElementById("new-account")

function logar() {

    const fd = new FormData(formNovaConta)
    const dadosFormulario = Object.fromEntries(fd)

    getLogin(dadosFormulario)
    .then(() => {
        showLogin()
        })
        .catch((erro) => {
            console.log(erro)
        })
}

function validarLogin() {

    const fd = new FormData(formNovaConta)
    const dadosFormulario = Object.fromEntries(fd)

    try {
        
    } catch (error) {
        
    }
}
