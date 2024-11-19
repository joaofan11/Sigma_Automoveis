document.addEventListener('DOMContentLoaded', carregarVendas);

// Função para carregar as vendas da API
function carregarVendas() {
    fetch('/vendas')
        .then(response => response.json())
        .then(data => {
            const tabela = document.querySelector('table tbody');
            tabela.innerHTML = '';
            data.forEach(venda => {
                const linha = document.createElement('tr');
                linha.innerHTML = `
                    <td>${venda.cliente_id}</td>
                    <td>${venda.vendedor_id}</td>
                    <td>${venda.veiculo_id}</td>
                    <td>${venda.valor_entrada}</td>
                    <td>${venda.valor_financiado}</td>
                    <td>${venda.valor_total}</td>
                    <td>${venda.data}</td>
                    <td>
                        <button onclick="editarVenda(${venda.id})">Editar</button>
                        <button onclick="excluirVenda(${venda.id})">Excluir</button>
                    </td>
                `;
                tabela.appendChild(linha);
            });
        });
}

// Função para adicionar ou editar uma venda
function salvarVenda(id = null) {
    const metodo = id ? 'PUT' : 'POST';
    const url = id ? `/vendas/${id}` : '/vendas';
    const dados = {
        numero: document.getElementById('numero').value,
        data: document.getElementById('data').value,
        cliente_id: document.getElementById('cliente').value,
        vendedor_id: document.getElementById('vendedor').value,
        veiculo_id: document.getElementById('veiculo').value,
        valor_entrada: document.getElementById('valorEntrada').value,
        valor_financiado: document.getElementById('valorFinanciado').value,
        valor_total: document.getElementById('valorTotal').value
    };

    fetch(url, {
        method: metodo,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    }).then(() => {
        carregarVendas();
        fecharModal();
    });
}

// Função para excluir uma venda
function excluirVenda(id) {
    fetch(`/vendas/${id}`, { method: 'DELETE' })
        .then(() => carregarVendas());
}
