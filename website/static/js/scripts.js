
document.addEventListener("DOMContentLoaded", function () {
  // Encontre o elemento <select> pelo nome ou id
  const selectElement = document.getElementById('client-select'); // Ou use '#id-do-select' se tiver um id específico

  if (selectElement && selectElement.options.length > 0) {
    // Acesse a primeira opção e altere seu conteúdo
    selectElement.options[0].text = "Selecione um cliente";
    selectElement.options[0].value = ""; // Opcional: ajuste o valor também
  }
});



document.addEventListener("DOMContentLoaded", function () {
  // Encontre o elemento <select> pelo nome ou id
  const selectElement = document.getElementById('product-select'); // Ou use '#id-do-select' se tiver um id específico

  if (selectElement && selectElement.options.length > 0) {
    // Acesse a primeira opção e altere seu conteúdo
    selectElement.options[0].text = "Selecione um produto";
    selectElement.options[0].value = ""; // Opcional: ajuste o valor também
  }
});



const priceInput = document.getElementById("price-input");
const formatter = new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" });

priceInput.addEventListener("blur", () => {
  let numericValue = priceInput.value.replace(/\D/g, ""); // Remove caracteres não numéricos
  if (numericValue) {
    const formattedValue = formatter.format(parseFloat(numericValue) / 100);
    priceInput.value = `R$ ${formattedValue.replace("R$", "").trim()}`; // Garante o "R$"
  } else {
    priceInput.value = "";
  }
});

