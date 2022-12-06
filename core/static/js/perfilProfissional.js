function toggleModal() {
    const modal = document.getElementById("modal");
    const body = document.getElementById("body-container");
  
    modal.classList.toggle("hidden");
    body.classList.toggle("overflow-hidden");
  }
  