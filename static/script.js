document.addEventListener("DOMContentLoaded", function() {
    const addToOrderButtons = document.querySelectorAll('input[type="submit"]');
  
    addToOrderButtons.forEach((button) => {
      button.addEventListener("click", (e) => {
        e.preventDefault();
        addToReceipt(e.target);
      });
    });
  });
  
  function addToReceipt(target) {
    const itemContainer = target.closest(".menu-item");
    const itemName = itemContainer.querySelector("h3").textContent;
    const itemPrice = parseFloat(itemContainer.querySelector(".price").textContent.slice(1));
    const itemQuantity = parseInt(itemContainer.querySelector("input[type='number']").value);
  
    if (itemQuantity > 0) {
      const receiptTable = document.querySelector("#receipt table");
      const existingRow = receiptTable.querySelector(`tr[data-item-name="${itemName}"]`);
  
      if (existingRow) {
        const existingQuantity = parseInt(existingRow.querySelector(".quantity").textContent);
        const newQuantity = existingQuantity + itemQuantity;
        existingRow.querySelector(".quantity").textContent = newQuantity;
        existingRow.querySelector(".item-total").textContent = `$${(itemPrice * newQuantity).toFixed(2)}`;
      } else {
        const newRow = document.createElement("tr");
        newRow.setAttribute("data-item-name", itemName);
        newRow.innerHTML = `
          <td>${itemName}</td>
          <td class="quantity">${itemQuantity}</td>
          <td class="item-total">$${(itemPrice * itemQuantity).toFixed(2)}</td>
        `;
        receiptTable.appendChild(newRow);
      }
  
      updateTotal(receiptTable);
    }
  }
  
  function updateTotal(receiptTable) {
    const itemTotals = receiptTable.querySelectorAll(".item-total");
    let total = 0;
  
    itemTotals.forEach((itemTotal) => {
      total += parseFloat(itemTotal.textContent.slice(1));
    });
  
    document.querySelector("#total").textContent = total.toFixed(2);
}
  