
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



