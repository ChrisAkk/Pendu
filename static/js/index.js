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

const toggleBtn = document.querySelector('.toggle-btn');
const circleOfBtn = document.querySelector('.circle')

if (toggleBtn && circleOfBtn) {
    toggleBtn.addEventListener('click', () => {
        toggleBtn.classList.toggle('on');
        circleOfBtn.classList.toggle('on');
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


