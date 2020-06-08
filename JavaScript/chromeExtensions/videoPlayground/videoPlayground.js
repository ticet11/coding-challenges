const theVideo = document.querySelector("video");
const playbackSpeed = theVideo.playbackRate;
const playing = false;

function speedUp(video) {
    video.playbackRate += 0.1;
}

function slowDown(video) {
    video.playbackRate -= 0.1;
}

function regularSpeed(video) {
    video.playbackRate = 1;
}

function playVid(video) {
    video.play();
}

function pauseVid(video) {
    video.pause();
}

document.addEventListener("keydown", (e) => {
    if (e.key === "j") {
        speedUp(theVideo);
    } else if (e.key === "k") {
        slowDown(theVideo);
    } else if (e.key === "l") {
        regularSpeed(theVideo);
    } else if (e.key === "n") {
        playVid(theVideo);
    } else if (e.key === "m") {
        pauseVid(theVideo);
    }
});