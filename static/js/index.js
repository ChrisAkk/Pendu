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