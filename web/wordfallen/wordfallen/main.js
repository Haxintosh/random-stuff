import { loadSVG } from 'pixi.js';
import './style.css'

const alphabetRegex = /Key[A-Z]/g;

let timeoutId = null;
addEventListener('keydown', handleKeydown)

function handleKeydown(event) {
  const key = event.code;
  if (key.match(alphabetRegex)) {
    console.log(event.key)
    popKey(event.key)
  }
}

function popKey(e){
  if (document.querySelector('.key')) {
    const oldKey = document.querySelector('.key');
    oldKey.classList.remove('key');
    oldKey.classList.add('key--old');
    clearTimeout(timeoutId);
    oldKey.animate({
      transform: ['translateY(0)', 'translateY(100vh)']
    }, { 
      duration: 500,
      easing: 'cubic-bezier(0.175, 0.885, 0.32, 1.275)',
      fill: 'forwards'
    }).finished.then(() => {
      oldKey.remove();
    });

  }
  let newKey = document.createElement('div');
  newKey.innerHTML = e;
  newKey.style.opacity = 0;
  newKey.classList.add('key');
  document.body.appendChild(newKey);
  newKey.animate({
    opacity: [0, 1]
  }, {
    duration: 200,
    easing: 'ease-in-out',
    fill: 'forwards'
  }).finished.then(anim => anim.commitStyles())

  timeoutId = setTimeout(() => {
    newKey.animate({
      transform: ['translateY(0)', 'translateY(100vh)']
    }, {
      duration: 500,
      easing: 'ease-in-out',
      fill: 'forwards'
    }).finished.then(() => console.log('finished'))
  }, 1000);
}
