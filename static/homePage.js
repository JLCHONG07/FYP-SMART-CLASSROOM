//Create a timeline for moving the nav bar left text
let tl = gsap.timeline({
    scrollTrigger: {
        trigger: '.contextHome',
        start: '0%',
        //speed for animation
        end: '80%',
        //repeat when back
        scrub: 1,
    },
});

//Create second timeline for moving the Smart Classroom words from middle to top left 
let tl2 = gsap.timeline({
    scrollTrigger: {
        trigger: '.contextHome',
        start: '0%',
        //speed for animation
        end: '80%',
        //repeat when back
        scrub: 1,
    },
});

//Create a timeline for welcome to and experience new learning environment
let tl4 = gsap.timeline({
    scrollTrigger: {
        trigger: '.contextHome',
        start: '0%',
        //speed for animation
        end: '10%',
        //repeat when back
        scrub: 1,


    },
});


//Create a timeline for buttons of home
let tl6 = gsap.timeline({
    scrollTrigger: {
        trigger: '.contextHome',
        start: '0%',
        //speed for animation
        end: '30%',
        //repeat when back
        scrub: 1,
    },
});

//Create a timeline for scroll words
let tl7 = gsap.timeline({
    scrollTrigger: {
        trigger: '.contextHome',
        start: '0%',
        //speed for animation
        end: '1%',
        //repeat when back
        scrub: 1,
    },
});

//Create a timeline for features come in 
let tl8 = gsap.timeline({
    scrollTrigger: {
        trigger: '.contextHome',
        start: '0%',
        //speed for animation
        end: '100%',
        //repeat when back
        scrub: 1,
    },
});

//create a timeline for features go out
let tl9 = gsap.timeline({
    scrollTrigger: {
        trigger: '.contextFeatures',
        start: '0%',
        //speed for animation
        end: '50%',
        //repeat when back
        scrub: 1,
    },
});

//create a timeline for team
let tl0 = gsap.timeline({
    scrollTrigger: {
        trigger: '.contextTeam',
        start: '0%',
        //speed for animation
        end: '20%',
        //repeat when back
        scrub: 1,


    },
});




//create timeline 3 for stick when scroll the Home
let tl3 = gsap.timeline({
    scrollTrigger: {
        trigger: '.contextHome',
        start: '0%',
        //speed for animation
        end: '300%',
        //trigger in 1 second
        scrub: 1,
        pin: ".firstPageRow2",
        pinSpacing: false,

    },
});

//var x = gsap.getProperty("#logo", "left");
//var y = gsap.getProperty("#logo", "right");
//console.log(x);
//console.log(y);

var y = window.scrollY + document.querySelector('.navbar').getBoundingClientRect().height;
var x = window.scrollX + document.querySelector('#logo').getBoundingClientRect().left;

console.log(y);
console.log(x);
//console.log(rect.top, rect.right, rect.bottom, rect.left);

//trigger the moving position from begin to end
tl.fromTo('.sliding-text', { y: 0 }, { y: -400 });
tl2.to('.firstPageRow2', { scale: 0.3, top: "2.5rem", left: "10rem", zIndex: 2 });
tl4.fromTo('.firstPageRow1', { scale: 1 }, { scale: 0.5, left: "-100%" });
tl4.fromTo('.firstPageRow3', { scale: 1 }, { scale: 0.5, left: "200%" });
tl6.fromTo('.buttons-position', { scale: 1 }, { scale: 0.5, opacity: 0, left: "100%" });
tl7.to('.scroll-words-position', { opacity: 0, top: "100%" });
tl8.fromTo('.feature-1', { scale: 0.5, opacity: "0%", }, { scale: 1.1, opacity: "100%" })
tl8.fromTo('.feature-2', { scale: 0.5, opacity: "0%" }, { scale: 1.1, opacity: "100%" })
tl9.fromTo('.feature-1', { opacity: "100%", }, { scale: 0.5, opacity: "0%" })
tl9.fromTo('.feature-2', { opacity: "100%" }, { scale: 0.5, opacity: "0%" })
tl0.fromTo('.team-container', { scale: 0.5, opacity: 0 }, { scale: 2.5, opacity: 100 })
    //tl.to('.firstPageRow2', { opacity: 0 });

const words = ["Environment", "Method", "Style"]

let cursor = gsap.to('.typing', { opacity: 0, ease: "power2.inOut", repeat: -1 })
let masterTl = gsap.timeline({
    repeat: -1

})


words.forEach(word => {
    let tl5 = gsap.timeline({ repeat: 1, yoyo: true, repeatDelay: 1, })
    tl5.to('.text', { duration: 1, text: word })
    masterTl.add(tl5)
})


const headerSections = gsap.utils.toArray('.invert-header');
/*
headerSections.forEach(section => {

    ScrollTrigger.create({
        trigger: section,
        start: 'top 10%',
        end: 'bottom 10%',
        toggleClass: {
            targets: '.custom-color-navbar ',
            className: 'white-nav-bar',

        },

        markers: true
    })


});
*/





const sections = document.querySelectorAll('section');
const navLi = document.querySelectorAll('nav .container-fluid ul li a.nav-link');
//console.log(navLi);
// console.log(sections);

window.addEventListener('scroll', () => {
    let current = "";
    //How much of y-axis is scrolled
    // console.log("Y"+pageYOffset);
    sections.forEach(section => {
        //To get the top height for each section
        const sectionTop = section.offsetTop;
        // console.log("top:"+sectionTop);
        //Total height of the section
        const sectionHeight = section.clientHeight;
        //console.log("section:"+sectionHeight);
        if (pageYOffset >= (sectionTop - sectionHeight / 3)) {
            current = section.getAttribute('id');

        }
    });
    //console.log(current);

    navLi.forEach(li => {
        li.classList.remove('active');
        console.log(li.classList.toString());
        if (li.classList.contains(current)) {
            console.log(li.classList.add('active'));
        } else {
            console.log("not contain");
        }

    });
})