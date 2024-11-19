function salvarVenda() {
    const dados = {
        numero: document.getElementById('codigo').value,
        data: document.getElementById('data').value,
        cliente_id: document.getElementById('cliente').value,
        vendedor_id: document.getElementById('vendedor').value,
        veiculo_id: document.getElementById('veiculo').value,
        valor: document.getElementById('valorTotal').value,
    };

    // Verificar se todos os campos estão preenchidos
    if (Object.values(dados).includes('')) {
        alert('Por favor, preencha todos os campos obrigatórios.');
        return;
    }

    fetch('/compras', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        carregarCompras();  // Atualiza a tabela sem precisar recarregar a página
    })
    .catch(error => console.error('Erro:', error));
}

function carregarCompras() {
    fetch('/compras')
    .then(response => response.json())
    .then(data => {
        const tabela = document.querySelector('table tbody');
        tabela.innerHTML = '';  // Limpa a tabela

        data.forEach(compra => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${compra.numero}</td>
                <td>${compra.cliente_id}</td>
                <td>${compra.vendedor_id}</td>
                <td>${compra.veiculo_id}</td>
                <td>${compra.valor}</td>
                <td><button onclick="editarVenda(${compra.id})">Editar</button></td>
                <td><button onclick="excluirVenda(${compra.id})">Excluir</button></td>
            `;
            tabela.appendChild(row);
        });
    })
    .catch(error => console.error('Erro:', error));
}

function editarVenda(id) {
    // Lógica para editar a venda, que pode abrir um modal com os dados preenchidos
    // Você pode pegar os dados da venda com o id do servidor e preenchê-los no modal
}

function excluirVenda(id) {
    if (confirm('Tem certeza que deseja excluir esta venda?')) {
        fetch(`/compras/${id}`, {
            method: 'DELETE',
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            carregarCompras();  // Atualiza a tabela após a exclusão
        })
        .catch(error => console.error('Erro:', error));
    }
}

// Chame a função de carregarCompras ao carregar a página
document.addEventListener('DOMContentLoaded', carregarCompras);

