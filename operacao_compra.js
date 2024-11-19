function salvarVenda() {
    const dados = {
        numero: document.getElementById('codigo').value,
        data: document.getElementById('data').value,
        cliente_id: document.getElementById('cliente').value,
        vendedor_id: document.getElementById('vendedor').value,
        veiculo_id: document.getElementById('veiculo').value,
        valor: document.getElementById('valorTotal').value,
    };

    fetch('/compras', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados),
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            window.location.reload(); // Atualiza a página
        })
        .catch(error => console.error('Erro:', error));
}

function carregarCompras() {
    fetch('/compras')
        .then(response => response.json())
        .then(data => {
            const tabela = document.querySelector('table tbody');
            tabela.innerHTML = ''; // Limpa a tabela
            data.forEach(compra => {
                const row = `
                    <tr>
                        <td>${compra.numero}</td>
                        <td>${compra.cliente_id}</td>
                        <td>${compra.vendedor_id}</td>
                        <td>${compra.veiculo_id}</td>
                        <td>${compra.valor}</td>
                        <td><button onclick="editarVenda(${compra.id})">Editar</button></td>
                        <td><button onclick="excluirVenda(${compra.id})">Excluir</button></td>
                    </tr>
                `;
                tabela.innerHTML += row;
            });
        })
        .catch(error => console.error('Erro:', error));
}

// Chame essa função ao carregar a página
carregarCompras();
