function showSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'flex'
}

function hideSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'none'
}

$(document).ready(function() {
    $('#id_cpf').mask('000.000.000-00', {reverse: false});
    $('.mask-cnpj').mask('00.000.000/0000-00', {reverse: false});
    $('#id_cep').mask('00000-000', {reverse: false});
    $('#id_identidade').mask('00.000.000', {reverse: false});
    $('#phone').mask('(00) 00000-0000');
    
});