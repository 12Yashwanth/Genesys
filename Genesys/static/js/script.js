let slides = document.querySelectorAll(".slide");
let index = 0;

function showSlide(i){
    slides.forEach(s => s.classList.remove("active"));
    slides[i].classList.add("active");
}

document.querySelector(".right").onclick = () =>{
    index = (index + 1) % slides.length;
    showSlide(index);
};

document.querySelector(".left").onclick = () =>{
    index = (index - 1 + slides.length) % slides.length;
    showSlide(index);
};
