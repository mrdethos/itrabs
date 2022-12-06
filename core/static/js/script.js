window.addEventListener('scroll', onScroll)

onScroll()
function onScroll() {
  showNavOnScroll()
}

function showNavOnScroll() {
  if (scrollY > 0) {
    header.classList.add('scroll')
  } else {
    header.classList.remove('scroll')
  }
}

document.getElementById("botaoperfil").onclick = function() {
  location.href = "{% url 'encontrarprofissionais.html' %}"
}