const toTop = document.querySelector("#btnScrollToTop");

window.addEventListener("scroll", () => {
    if(window.pageYOffset > 100){
        toTop.classList.add("active");
    }else{
        toTop.classList.remove("active");
    }
});
btnScrollToTop.addEventListener("click", function (){
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
    })
})