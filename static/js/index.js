// boutons pour afficher configuraton

const btnConfiguration = document.querySelector('.btn-configuration')
const menuConfiguration = document.querySelector('.configuration-page')

if (btnConfiguration && menuConfiguration) {
    btnConfiguration.addEventListener('click', (e) => {
        e.stopPropagation();
        menuConfiguration.classList.toggle('on');
    });

    document.addEventListener('click', (e) => {
        if (!menuConfiguration.contains(e.target) && menuConfiguration.classList.contains('on')) {
            menuConfiguration.classList.remove('on');
        };
    });
    
    document.addEventListener('scroll', () => {
        if (menuConfiguration.classList.contains('on')) {
            menuConfiguration.classList.remove('on');
        };
    })

    
}

const menuPercher = document.querySelector('.menu-start');
const btnAddPercher = document.querySelector('.welcome-btn');
const btnRemovePercher = document.querySelector('.back-btn-1')

if (btnAddPercher) {
    btnAddPercher.addEventListener('click', () => {
        setTimeout(() => {
            menuPercher.classList.add('visible');
        }, 500)
    })
}

if (btnRemovePercher) {
    btnRemovePercher.addEventListener('click', () => {
        menuPercher.classList.remove('visible')
    })
}

// Les boutons de theme

const btnTheme = document.querySelectorAll('.btn-theme')
const btnFinal = document.querySelector('.jouer-btn')
const inputThemeSelected = document.querySelector('#hidden-theme')

if (btnFinal) { btnFinal.disabled = true; }

let theme = [];

btnTheme.forEach(bouton => {
    bouton.addEventListener('click', () => {
        
        const nomTheme = bouton.dataset.theme;
        bouton.classList.toggle('selected');

        if (bouton.classList.contains('selected')) {
            theme.push(nomTheme)
        } else {
            theme = theme.filter(value => value !== nomTheme)
        }

        inputThemeSelected.value = theme.join(',')

        if (theme.length === 0) {
            btnFinal.disabled = true;
        } else {
            btnFinal.disabled = false;
        }
    });
})

// Les boutons toggle

const toggleBtn1 = document.querySelector('.toggle-btn-1');
const circleOfBtn1 = document.querySelector('.circle-1');
const inputIndiceSelected = document.querySelector('#hidden-indice');

if (toggleBtn1 && circleOfBtn1) {
    toggleBtn1.addEventListener('click', () => {
        toggleBtn1.classList.toggle('on');
        circleOfBtn1.classList.toggle('on');

        if (toggleBtn1.classList.contains('on')) {
            inputIndiceSelected.value = 'on';
        } else {
            inputIndiceSelected.value = 'off';
        }
    })
}

const toggleBtn2 = document.querySelector('.toggle-btn-2');
const circleOfBtn2 = document.querySelector('.circle-2');
const sliderCaractere = document.querySelector('.slider-2');
const inputAleatoireSelected = document.querySelector('#hidden-aleatoire');

if (toggleBtn2 && circleOfBtn2) {
    toggleBtn2.addEventListener('click', () => {
        toggleBtn2.classList.toggle('on');
        circleOfBtn2.classList.toggle('on');

        if (toggleBtn2.classList.contains('on')) {
            sliderCaractere.classList.add('disabled');
            inputAleatoireSelected.value = 'on';
        } else {
            sliderCaractere.classList.remove('disabled');
            inputAleatoireSelected.value = 'off';
        }
    })
}

// etincelle 

let sparkEnabled = true;

document.addEventListener('mousemove', (e) => {
    if (!sparkEnabled) return;

    const spark = document.createElement('div');
    spark.classList.add('spark');
    spark.style.left = e.pageX + 'px';
    spark.style.top = e.pageY + 'px';
    document.body.appendChild(spark);

    setTimeout(() => {
        spark.remove();
    }, 600);
});

// bouton clavier 

let btnLetters = document.querySelectorAll('.btn-letters');
let letter;

window.focus();

window.addEventListener('keydown', (event) => {
    if (winJs === 'true'){
        return;
    }

    letter = event.key.toUpperCase();
    console.log(letter);
    
    btnLetters.forEach(button => {
        if (button.value === letter) {
            button.focus()
            button.click()
        }
    })
})

// bouton indice 

const btnIndice = document.querySelector('.indice-btn');
const indice = document.querySelector('.indice')

if (btnIndice) {
    btnIndice.addEventListener('click', () => {
        indice.classList.toggle('on');
    })
}
