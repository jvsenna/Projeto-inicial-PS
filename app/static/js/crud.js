/**
 * Motor genérico de telas CRUD do JobReady.
 * Cada página de tela (ex: usuarios/list.html) define um objeto `pageConfig`
 * com o endpoint da API e os campos do formulário, e chama initCrudPage().
 *
 * Isso cumpre o requisito de que as telas do frontend chamem as rotas
 * de CRUD já implementadas na API (fetch para /api/<recurso>).
 */

function initCrudPage(config) {
  const state = { items: [], editingId: null };

  const tableBody = document.querySelector("#crud-table tbody");
  const emptyState = document.querySelector("#empty-state");
  const modalBackdrop = document.querySelector("#crud-modal-backdrop");
  const modalTitle = document.querySelector("#crud-modal-title");
  const form = document.querySelector("#crud-form");
  const alertBox = document.querySelector("#crud-alert");
  const btnNovo = document.querySelector("#btn-novo");
  const btnCancelar = document.querySelector("#btn-cancelar");

  function showAlert(msg, type = "error") {
    alertBox.textContent = msg;
    alertBox.className = `alert alert-${type === "error" ? "error" : "success"}`;
    alertBox.style.display = "block";
    setTimeout(() => { alertBox.style.display = "none"; }, 4000);
  }

  function renderRow(item) {
    const tr = document.createElement("tr");
    const cells = config.columns.map(col => {
      const value = col.render ? col.render(item) : (item[col.key] ?? "—");
      return `<td>${value}</td>`;
    }).join("");
    tr.innerHTML = `
      ${cells}
      <td class="actions-cell">
        <button class="btn btn-secondary btn-sm" data-action="edit" data-id="${item.id}">Editar</button>
        <button class="btn btn-danger btn-sm" data-action="delete" data-id="${item.id}">Excluir</button>
      </td>`;
    return tr;
  }

  async function carregarLista() {
    const res = await fetch(config.apiUrl);
    state.items = await res.json();
    tableBody.innerHTML = "";
    if (state.items.length === 0) {
      emptyState.style.display = "block";
    } else {
      emptyState.style.display = "none";
      state.items.forEach(item => tableBody.appendChild(renderRow(item)));
    }
  }

  function abrirModal(item = null) {
    state.editingId = item ? item.id : null;
    modalTitle.textContent = item ? `Editar ${config.singular}` : `Novo ${config.singular}`;
    form.reset();
    if (item) {
      config.fields.forEach(f => {
        const el = form.elements[f.name];
        if (el) el.value = item[f.name] ?? "";
      });
    }
    modalBackdrop.classList.add("open");
  }

  function fecharModal() {
    modalBackdrop.classList.remove("open");
    state.editingId = null;
  }

  async function salvar(event) {
    event.preventDefault();
    const dados = {};
    config.fields.forEach(f => {
      const el = form.elements[f.name];
      let value = el.value;
      if (f.type === "number" && value !== "") value = Number(value);
      if (value !== "") dados[f.name] = value;
    });

    const editing = state.editingId !== null;
    const url = editing ? `${config.apiUrl}/${state.editingId}` : config.apiUrl;
    const method = editing ? "PUT" : "POST";

    const res = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados),
    });
    const payload = await res.json();

    if (!res.ok) {
      showAlert(payload.erro || "Não foi possível salvar.");
      return;
    }
    showAlert(editing ? `${config.singular} atualizado com sucesso.` : `${config.singular} criado com sucesso.`, "success");
    fecharModal();
    carregarLista();
  }

  async function excluir(id) {
    if (!confirm(`Tem certeza que deseja excluir este registro?`)) return;
    const res = await fetch(`${config.apiUrl}/${id}`, { method: "DELETE" });
    const payload = await res.json();
    if (!res.ok) {
      showAlert(payload.erro || "Não foi possível excluir.");
      return;
    }
    showAlert(`${config.singular} excluído com sucesso.`, "success");
    carregarLista();
  }

  tableBody.addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-action]");
    if (!btn) return;
    const id = Number(btn.dataset.id);
    if (btn.dataset.action === "edit") {
      const item = state.items.find(i => i.id === id);
      abrirModal(item);
    } else if (btn.dataset.action === "delete") {
      excluir(id);
    }
  });

  btnNovo.addEventListener("click", () => abrirModal());
  btnCancelar.addEventListener("click", fecharModal);
  modalBackdrop.addEventListener("click", (e) => { if (e.target === modalBackdrop) fecharModal(); });
  form.addEventListener("submit", salvar);

  carregarLista();
}
