const root = document.documentElement;
const animationDuration = getComputedStyle(root).getPropertyValue('--animation-duration');

const randomNumber = (Max = 255, Min = 55) => {
    return Math.floor(Math.random() * (Max - Min)) + Min;
}

const updateColor = () => {
    root.style.setProperty(
      "--color",
      `rgb(${randomNumber()},
           ${randomNumber()}, 
           ${randomNumber()})`
    );
}

setInterval(() => {
    updateColor();
}, animationDuration)
