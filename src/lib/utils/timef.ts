export function timerString(sec: number) {
    const mins = Math.floor(sec / 60);
    const secs = sec % 60;
    
    if (mins == 0) return secs.toFixed(1);
    else {
        let secsStr = secs.toFixed(1);
        if (secsStr.length == 3) secsStr = `0${secsStr}`;
        return `${mins}:${secsStr}`;
    }
}