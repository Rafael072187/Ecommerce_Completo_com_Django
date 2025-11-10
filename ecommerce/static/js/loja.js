// Script de ordenar
function redirectToPage() {
  var selectElement = document.getElementsByClassName('produtos__select')[0];
  var selectedOption = selectElement.options[selectElement.selectedIndex].value;
  if (selectedOption) {
    window.location.href = selectedOption;
  }
}

// === Scripts do Menu Lateral ===

// 🟦 Destacar Tamanho Selecionado
document.querySelectorAll('.menu__tamanho .menu__checkbox').forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    document.querySelectorAll('.menu__tamanho .menu__tamanho-quadrado').forEach(function (div) {
      div.style.color = '';
      div.style.borderColor = '';
      div.style.backgroundColor = '';
    });
    var div = this.previousElementSibling;
    if (this.checked) {
      div.style.color = '#fff';
      div.style.borderColor = '#6495ED';
      div.style.backgroundColor = '#6495ED';
    }
  });
});

// 🟦 Destacar Tipo Selecionado
document.querySelectorAll('.menu__categoria .menu__checkbox').forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    document.querySelectorAll('.menu__categoria .menu__categoria-quadrado').forEach(function (div) {
      div.style.color = '';
      div.style.backgroundColor = '';
    });
    var div = this.previousElementSibling.previousElementSibling;
    if (this.checked) {
      div.style.backgroundColor = '#6495ED';
      div.style.borderColor = '#6495ED';
    }
  });
});

// === Expansão do menu lateral ===
document.querySelectorAll(".menu__expansivel-cabecalho").forEach(function (ele) {
  ele.addEventListener("click", function () {
    ele.parentElement.classList.toggle("menu__expansivel--aberto");
  });
});

// === Abrir / Fechar filtro lateral ===
const fecharFiltro = document.querySelector(".menu__fechar-filtro");
const abrirFiltro = document.querySelector(".produtos__cabecalho-filtrar");

if (fecharFiltro && abrirFiltro) {
  fecharFiltro.addEventListener("click", () => document.body.classList.remove("filtro-aberto"));
  abrirFiltro.addEventListener("click", () => document.body.classList.add("filtro-aberto"));
}

// === 🎚 Faixa de preço dinâmica ===
const fromSlider = document.getElementById('fromSlider');
const toSlider = document.getElementById('toSlider');
const fromInput = document.getElementById('preco_minimo');
const toInput = document.getElementById('preco_maximo');

// Atualiza os valores e a cor da linha conforme movimento
function fillSlider(from, to, sliderColor, rangeColor, controlSlider) {
  const rangeDistance = to.max - to.min;
  const fromPosition = from.value - to.min;
  const toPosition = to.value - to.min;
  controlSlider.style.background = `linear-gradient(
    to right,
    ${sliderColor} 0%,
    ${sliderColor} ${(fromPosition / rangeDistance) * 100}%,
    ${rangeColor} ${(fromPosition / rangeDistance) * 100}%,
    ${rangeColor} ${(toPosition / rangeDistance) * 100}%,
    ${sliderColor} ${(toPosition / rangeDistance) * 100}%,
    ${sliderColor} 100%)`;
}

function updateInputs() {
  const from = parseInt(fromSlider.value);
  const to = parseInt(toSlider.value);
  fromInput.value = from;
  toInput.value = to;
  fillSlider(fromSlider, toSlider, '#ccc', '#4CAF50', toSlider);
}

function updateSliders() {
  const from = parseInt(fromInput.value);
  const to = parseInt(toInput.value);
  fromSlider.value = from;
  toSlider.value = to;
  fillSlider(fromSlider, toSlider, '#ccc', '#4CAF50', toSlider);
}

fromSlider.addEventListener('input', updateInputs);
toSlider.addEventListener('input', updateInputs);
fromInput.addEventListener('input', updateSliders);
toInput.addEventListener('input', updateSliders);

// Inicializa o gradiente verde
if (fromSlider && toSlider) fillSlider(fromSlider, toSlider, '#ccc', '#4CAF50', toSlider);
