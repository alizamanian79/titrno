function navigateToPage() {
  const selectElement = document.getElementById("pageSelect");
  const selectedValue = selectElement.value;
  if (selectedValue) {
    window.location.href = selectedValue;
  }
}
