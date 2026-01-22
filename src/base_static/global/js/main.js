/*=============== SHOW MENU ===============*/

const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/* Show menu */
if(navToggle){
   navToggle.addEventListener('click', () =>{
      navMenu.classList.add('show-menu')
   })
}

/* Hide menu */
if(navClose){
   navClose.addEventListener('click', () =>{
      navMenu.classList.remove('show-menu')
   })
}



/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav__link')
const linkAction = ()=>{
   const navMenu = document.getElementById('nav-menu')
   navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))


/*=============== ADD BLUR HEADER ===============*/
const blurHeader = ()=>{
   const header = document.getElementById('header')

   this.scrollY >= 50 ? header.classList.add('blur-header')
                      : header.classList.remove('blur-header')
}

window.addEventListener('scroll', blurHeader)



/*=============== EMAIL JS ===============*/


/*=============== SHOW SCROLL UP ===============*/ 
const scrollUp = () =>{
	const scrollUp = document.getElementById('scroll-up')
   // Add the .scroll-header class if the bottom scroll of the viewport is greater than 350
	this.scrollY >= 350 ? scrollUp.classList.add('show-scroll')
						     : scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll('section[id]')

// Link the ID of each section (section id="home") to each link (a href="#home") 
// and activate the link with the class .active-link
const scrollActive = () => {
   // We get the position by scrolling down
   const scrollY = window.scrollY

   sections.forEach(section => {
      const id = section.id, // id of each section
            top = section.offsetTop - 50, // Distance from the top edge
            height = section.offsetHeight, // Element height
            link = document.querySelector('.nav__menu a[href*=' + id + ']') // id nav link

      if(!link) return

      link.classList.toggle('active-link', scrollY > top && scrollY <= top + height)
   })
}
window.addEventListener('scroll', scrollActive)

/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
   origin: 'top',
   distance: '60px',
   duration: 2500,
   delay: 400,
   //reset: true //animation repeat
})

sr.reveal(`.home__data, .experience, .skills, .contact__container`)
sr.reveal(`.home__img`, {delay: 600})
sr.reveal(`.home__scroll`, {delay: 800})
sr.reveal(`.work__card, .services__card`, {interval: 100})
sr.reveal(`.about__content`, {origin:'right'})
sr.reveal(`.about__img`, {origin:'left'})