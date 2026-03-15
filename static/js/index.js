const btnConfiguration = document.querySelector('.btn-configuration')
const menuConfiguration = document.querySelector('.configuration-page')

if (btnConfiguration) {
    btnConfiguration.addEventListener('click', () => {
        menuConfiguration.classList.toggle('on')
    } )
}

const btnTheme = document.querySelectorAll('.btn-theme')
const btnFinal = document.querySelector('.jouer-btn')

if (btnFinal) { btnFinal.disabled = true; }

btnTheme.forEach(bouton => {
    bouton.addEventListener('click', () => {
        bouton.classList.toggle('selected');

        const btnThemeChoice = document.querySelector('.btn-theme.selected');

        if (!btnThemeChoice) {
            btnFinal.disabled = true;
        } else {
            btnFinal.disabled = false;
        }
    });
})

const toggleBtn1 = document.querySelector('.toggle-btn-1');
const circleOfBtn1 = document.querySelector('.circle-1')

if (toggleBtn1 && circleOfBtn1) {
    toggleBtn1.addEventListener('click', () => {
        toggleBtn1.classList.toggle('on');
        circleOfBtn1.classList.toggle('on');
    })
}

const toggleBtn2 = document.querySelector('.toggle-btn-2');
const circleOfBtn2 = document.querySelector('.circle-2');
const sliderCaractere = document.querySelector('.slider-2');

if (toggleBtn2 && circleOfBtn2) {
    toggleBtn2.addEventListener('click', () => {
        toggleBtn2.classList.toggle('on');
        circleOfBtn2.classList.toggle('on');

        if (toggleBtn2.classList.contains('on')) {
            sliderCaractere.classList.add('disabled');
        } else {
            sliderCaractere.classList.remove('disabled');
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


